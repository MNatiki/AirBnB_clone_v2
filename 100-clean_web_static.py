#!/usr/bin/python3
"""
The `deploy` function creates a compressed archive file of the
`web_static` folder and saves it in the `versions` for deployment
"""
from fabric.api import *
env.hosts = ['54.164.28.87', '100.26.164.50']
from datetime import datetime
import os


def do_clean(number=0):
    today = datetime.now()
    created_at = []
    for i in os.listdir("versions"):
        created_at.append(datetime.fromtimestamp(os.stat("versions/" + i).st_ctime))
    recent = []
    latest = datetime(2000, 1, 9, 2, 34, 35)
    for i in created_at:
        if i > latest:
            print("latest")
            latest = i
            if len(recent) < 2:
                print("recent")
                recent.append(latest)
    


do_clean()
