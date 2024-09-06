#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7263361239:AAE8R_1dFE1xcRP9diWK06Aj8hR5r4GpRqI")
    API_ID = int(os.environ.get("API_ID", "23031620"))
    API_HASH = os.environ.get("API_HASH", "31cb00c1cbe580394778b43105864bca")
    AUTH_USERS = os.environ.get("AUTH_USERS", "502980590")
