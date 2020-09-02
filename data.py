# TODO: use gandi get only api key to read all dns record

HOSTS = {
    "140.118.9.222": "網站",
    "192.168.0.11": "大考",
    "192.168.0.12": "旗艦",
}


def get_name_by_ip(ip: str) -> str:
    return HOSTS.get(ip, "")


# @ 1800 IN A 140.118.9.222 -> @
# cdr 1800 IN CNAME cgm.im.
# ceec 1800 IN A 140.118.109.84 -> xn--pss471g
# flagship 1800 IN A 140.118.110.127 -> xn--igvr94d
# sheiun 1800 IN A 140.118.109.240 -> X
# webmail 1800 IN CNAME cgm.im.
# xn--igvr94d 1800 IN CNAME flagship.cgm.im.
# xn--pss471g 1800 IN CNAME ceec.cgm.im.

# TODO: check all services
# use nmap?

## 取所有 A 對應的 IP 與 domain 就可以取得唯一主機
# 再針對這個 domain -> 取得 CNAME -> 找到中文名 (punnycode)
# 沒有中文 punnycode 就不要
