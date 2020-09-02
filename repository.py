import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Union

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


TIME_FMT = r"%Y-%m-%d %H:%M:%S"


@dataclass
class Service:
    name: str  # format "{host}-{service}"
    protocol: str  # https / ssh / ...
    port: str  # 443 / 8000 / ...


@dataclass
class Host:
    ip: str  # NOTE: unique
    name: str = "?"
    metrics: dict = field(default_factory=dict)
    last_update: datetime = field(
        default_factory=datetime.now,
        init=False,
    )


class Repository:
    interval: int = 5 * 60  # 5min
    _hosts: Dict[str, Host] = {}  # {ip: host}

    def __init__(self, *args, **kwargs):
        for key, value in kwargs:
            setattr(self, key, value)

    def auto_check_and_deregister(self):
        now = datetime.now()
        for ip, host in self._host.items():
            # check last update is 2 times interval
            if now > host.last_update + timedelta(seconds=2 * self.interval):
                logger.info(f"{host.name} is outedated, deregister it now!")
                self.deregister(ip)

    @property
    def services(self) -> List[Service]:
        """Aggregate services

        Returns:
            List[Service]: All services
        """
        raise NotImplementedError()
        svcs = []
        for _, host in self._hosts.items():
            svcs.extend()
        return svcs

    @property
    def metrics(
        self,
    ) -> Dict[str, Dict[str, Union[str, Dict[str, Union[str, float, int]]]]]:
        """Aggregate metrics

        Returns:
            Dict[str, Dict[str, Union[str, Dict[str, Union[str, float, int]]]]]:
            {
              "網站": {
                "os": "Ubuntu 20.04.1 LTS",
                "ip": "140.118.9.222",
                "cpu": { "total": 100, "used": 6.6, "unit": "%" },
                "ram": {
                  "total": 3.7190513610839844,
                  "used": 2.2864608764648438,
                  "unit": "GB"
                },
                "disks": {
                  "/": {
                    "total": 907.6402473449707,
                    "used": 31.06873321533203,
                    "unit": "GB"
                  }
                },
                "vram": {},
                "net": { "total": 20, "used": 0.21386544965207577, "unit": "GB" },
                "domain": "cgm.im"
              },
              "旗艦": {
                "os": "Ubuntu 18.04.4 LTS",
                "ip": "140.118.110.127",
                "cpu": { "total": 100, "used": 74.2, "unit": "%" },
                "ram": {
                  "total": 31.228492736816406,
                  "used": 3.3500404357910156,
                  "unit": "GB"
                },
                "disks": {
                  "/": {
                    "total": 116.37757873535156,
                    "used": 61.42502212524414,
                    "unit": "GB"
                  },
                  "/mnt/sdb1": {
                    "total": 931.5107383728027,
                    "used": 340.91260528564453,
                    "unit": "GB"
                  }
                },
                "vram": {
                  "0: GeForce RTX 2080 Ti": {
                    "total": 10.7578125,
                    "used": 0.025390625,
                    "unit": "GB"
                  }
                },
                "net": { "total": 20, "used": 0.021168168634176254, "unit": "GB" },
                "domain": "flagship.cgm.im"
              },
              "大考": {
                "os": "Windows 10.0.19041",
                "ip": "140.118.109.84",
                "cpu": { "total": 100, "used": 0.6, "unit": "%" },
                "ram": {
                  "total": 11.909080505371094,
                  "used": 5.724323272705078,
                  "unit": "GB"
                },
                "disks": {
                  "C:\\": {
                    "total": 930.4313163757324,
                    "used": 121.89962387084961,
                    "unit": "GB"
                  }
                },
                "vram": {
                  "0: GeForce GTS 450": { "total": 1, "used": 0.1025390625, "unit": "GB" }
                },
                "net": { "total": 20, "used": 0.014969858340919018, "unit": "GB" },
                "domain": "ceec.cgm.im"
              }
            }
        """
        return {h.ip: h.metrics for _, h in self._hosts.items()}

    @property
    def hosts(self) -> List[Host]:
        return list(self._hosts.keys())

    def get_host(self, ip: str) -> Host:
        return self.hosts[ip]

    def is_host_exist(self, ip: str) -> bool:
        return ip in self._hosts.keys()

    def register(self, host: Host):
        self._hosts[host.ip] = host

    def deregister(self, ip: str):
        del self._hosts[ip]

    def update(self, ip: str, metrics: dict):
        # TODO: last_update
        self._hosts[ip].metrics = metrics


# NOTE: frontend need to know some fixed tabs
if __name__ == "__main__":
    repo = Repository()
