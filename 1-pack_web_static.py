#!/usr/bin/python3
"""
The `do_pack()` function creates a compressed archive file of the
`web_static` folder and saves it in the `versions` directory
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    The function `do_pack()` creates a compressed archive file of the
    `web_static` folder and saves it in the `versions` directory, and
    then prints the path and size of the created archive file.
    """
    today = datetime.now()
    name = "web_static_" + str(today.year) + str(today.month) + \
        str(today.day) + str(today.hour) + str(today.minute) + \
        str(today.second) + ".tgz"
    local("mkdir -p versions")
    local(f'tar -cvzf versions/{name}.tgz web_static')
    # print(name)
    try:
        print(f"web_static packed: versions/{name} -> \
              {os.get.path.getsize(os.getcwd() + '/versions/' + name)}Bytes")
    except Exception:
        return None
    return '/versions/' + name
