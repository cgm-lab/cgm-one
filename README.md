# CGM One Backend

> [Frontend](https://github.com/cgm-lab/cgm-one/tree/master/frontend)

## Prerequisite

- Python 3.7+ (for backend)
  - pip3 (package manager)
- Node.js v12+ (for frontend)
  - yarn v1.21+ (package manager)
  - Quasar v1 (cli)

## Install

```bash
pip install -r requirements.txt  # backend
# frontend
cd frontend
yarn
```

## Development

- Backend (require build frontend first if you want to view spa web)

```bash
python app.py
```

- Frontend only

```bash
cd frontend
quasar dev -m pwa
```

## Production

```bash
# build frontend
cd frontend
quasar build
# run server
cd ..
python app.py
```
