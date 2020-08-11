from datetime import datetime

import grequests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi_utils.tasks import repeat_every
from starlette.middleware.cors import CORSMiddleware

from data import CACHED_METRICS, HOSTS

LAST_UPDATE = ""
app = FastAPI()


@app.on_event("startup")
@repeat_every(seconds=60 * 5, raise_exceptions=True)
def update_cache() -> None:
    def exception_handler(request, exception):
        print(request.url, exception)

    reqs = (
        grequests.get(f"http://{value['ip']}:9999/api", timeout=2)
        for name, value in HOSTS.items()
    )
    names = list(HOSTS.keys())
    ress = grequests.map(reqs, exception_handler=exception_handler)
    data = {name: res.json() for name, res in dict(zip(names, ress)).items() if res}

    for name, value in data.items():
        data[name]["domain"] = HOSTS[name]["domain"]

    global CACHED_METRICS, LAST_UPDATE
    CACHED_METRICS = data
    LAST_UPDATE = datetime.now().strftime("%H:%M:%S")

    print(LAST_UPDATE, CACHED_METRICS)


@app.get("/api/metrics")
def metrics():
    return CACHED_METRICS


@app.get("/api/hosts")
def hosts():
    return HOSTS


@app.get("/api/lastUpdate")
def last_update():
    return {"lastUpdate": LAST_UPDATE}


app.mount(
    "/static", StaticFiles(directory="frontend/dist/spa"), name="static",
)


@app.get("/", include_in_schema=False)
def root():
    return FileResponse("frontend/dist/spa/index.html", media_type="text/html")


if True:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
