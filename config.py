#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Config Module.
#

DEBUG = False
# WIZARD_GENERATED = '2018年 04月 10日 星期二 15:23:32 CST'

SITE_NAME = 'SSLand'
HTTP_PORT = 8000

SECRET_KEY = '8cLNhJCHQAlw7oVTKGx42roIK3yc3875bjaALfIdxzE='
DATABASE_FILENAME = 'db.sqlite3'

# Note: more setting about Django can be configured in `web/settings.py`

MODULES = {
    "Shadowsocks": {
        # see /service/Shadowsocks.py
        "executable": "ssserver",
        "config-file": "/etc/shadowsocks.json",
        "manager-address": "/var/run/shadowsocks-manager.sock",
    },

    # # Uncomment these to enable pptpd
    # "PPTP": {
    #     "executable": "service pptpd",
    #     "config-file": "/etc/ppp/chap-secrets"
    # }
}
