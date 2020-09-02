import unittest

from repository import Host, Repository


class TestApiUsage(unittest.TestCase):
    def setUp(self):
        self.repo = Repository()
        self.assertTrue(self.repo)

    def test_add_host(self):
        host = Host(
            ip="140.118.9.222",
            name="網站",
            metrics={},
        )
        self.repo.register(host)

    def test_update_host(self):
        self.repo.update(
            "140.118.9.222",
            {
                "os": "Ubuntu 20.04.1 LTS",
                "ip": "140.118.9.222",
                "cpu": {"total": 100, "used": 6.6, "unit": "%"},
                "ram": {
                    "total": 3.7190513610839844,
                    "used": 2.2864608764648438,
                    "unit": "GB",
                },
                "disks": {
                    "/": {
                        "total": 907.6402473449707,
                        "used": 31.06873321533203,
                        "unit": "GB",
                    }
                },
                "vram": {},
                "net": {"total": 20, "used": 0.21386544965207577, "unit": "GB"},
                "domain": "cgm.im",
            },
        )
