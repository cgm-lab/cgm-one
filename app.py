from dataclasses import asdict
from json import loads
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi_utils.tasks import repeat_every
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from data import get_name_by_ip
from repository import Host, Repository

app = FastAPI()
repo = Repository()


@app.get("/api/hosts/{ip}")
def read_host(ip: str) -> List[Host]:
    return repo.get_host(ip)


@app.get("/api/hosts")
def read_hosts() -> List[Host]:
    return repo.hosts


@app.post("/api/hosts", status_code=status.HTTP_201_CREATED)
async def create_host(request: Request):
    metrics = loads(await request.body())
    host = Host(
        ip=request.client.host,
        name=get_name_by_ip(request.client.host),
        metrics=metrics,
    )
    repo.register(host)
    return asdict(host)


@app.put("/api/hosts")
async def update_host(request: Request):
    metrics = loads(await request.body())
    repo.update(request.client.host, metrics)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.delete("/api/hosts")
async def delete_host(request: Request):
    repo.deregister(request.client.host)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/api/metrics")
def read_metrics():
    return repo.metrics


app.mount("/static", StaticFiles(directory="frontend/dist/pwa"), name="static")


@app.get("/", include_in_schema=False)
def root():
    return FileResponse("frontend/dist/pwa/index.html", media_type="text/html")

@app.get("/static", include_in_schema=False)
def re_root():
    url = app.url_path_for("root")
    return RedirectResponse(url)


def is_ip_valid(ip: str):
    return ip.startswith("140.118") or ip.startswith("192.168")


@app.middleware("http")
async def verify_client_ip(request: Request, call_next):
    if request.method != "GET" and not is_ip_valid(request.client.host):
        # NOTE: only allow specific computers to do CUD
        return Response(status_code=403)
    response = await call_next(request)
    return response


@app.on_event("startup")
@repeat_every(seconds=5 * 60)  # 5 min
def auto_check_and_deregister() -> None:
    repo.auto_check_and_deregister()


if __name__ == "__main__":
    DEBUG = True

    if DEBUG:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    uvicorn.run(app, host="0.0.0.0")
