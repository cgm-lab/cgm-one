# TODO: use gandi get only api key to read all dns record

HOSTS = {
    "網站": {"domain": "cgm.im", "ip": "140.118.9.222"},
    "旗艦": {"domain": "flagship.cgm.im", "ip": "140.118.110.127"},
    "大考": {"domain": "ceec.cgm.im", "ip": "140.118.109.84"},
}

CACHED_DATA = {}

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
