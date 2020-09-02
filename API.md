# New API

## Hosts

- api/hosts
  - GET
    - For `frontend` to know how many hosts
  - POST (create host and its metrics)
    - `name` needed, only allow 192.168 or 140.118
    - `ip` verify needed
  - PUT (update host metrics)
    - `ip` verify needed
  - DELETE (delete host)
    - `ip` verify needed

## Metrics

- api/metrics
  - GET

## Services

- api/services
  - GET
