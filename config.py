#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8477391358:AAEYn4j2azXBse60zosNCiVCSMFWhUTNyyk")
    API_ID = int(os.environ.get("API_ID", "20432564"))
    API_HASH = os.environ.get("API_HASH", "6efd58342f75a088f8a7b4a15bdd35cd")
    AUTH_USERS = "8277882193"


