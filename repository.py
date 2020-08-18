import logging
from datetime import datetime, timedelta
from typing import Dict, List, Union
from uuid import uuid4

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


TIME_FMT = r"%Y-%m-%d %H:%M:%S"

# NOTE: also check ip when check token


class Service:
    name: str  # format "{machine}-{service}"
    protocol: str  # https / ssh / ...
    port: str  # 443 / 8000 / ...


class Host:
    name: str
    ip: str
    metrics: dict
    services: List[Service]  # XXX: auto scan by server or ?
    last_update: str  # format follow `TIME_FMT`


class Repository:
    interval: int = 5 * 60  # 5min
    hosts: Dict[str, Host] = {}

    def __init__(self, *args, **kwargs):
        for key, value in kwargs:
            setattr(self, key, value)

    def auto_check_and_deregister(self):
        now = datetime.now()
        for token, host in self.hosts:
            last_update = datetime.strptime(host.last_update, TIME_FMT)
            # check last update is 2 times interval
            if now > last_update + timedelta(seconds=2 * self.interval):
                logger.info(f"{host.name} is outedated, deregister it now!")
                self.deregister(token)

    @property
    def services(self) -> List[Service]:
        svcs = []
        for token, host in self.hosts:
            svcs.extend(host.services)
        return svcs

    def is_host_exist(self, token: str, ip: str = "") -> bool:
        if ip:
            for token, host in self.hosts:
                if host.ip == ip:
                    raise LookupError(f"{ip} is already registered in repository!")
        return token in self.hosts.keys()

    def register(self, host: Host):
        # XXX: client forget token?
        token = str(uuid4())
        self.hosts[token] = host

    def update(self, token: str, metrics: dict):
        self.hosts[token].metrics = metrics

    def deregister(self, token: str):
        # TODO: support host input
        del self.hosts[token]


# NOTE: frontend need to know some fixed tabs

if __name__ == "__main__":
    repo = Repository()
