#!/usr/bin/python3
"""
_pack()` function creates a compressed archive file of the
`web_static` folder and saves it in the `versions` directory
"""
from fabric.api import *
from datetime import datetime
import os


@runs_once
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
    print("Packing web_static to versions/{}".format(name))
    local("mkdir -p versions")
    result = local('tar -cvzf versions/{} web_static'.format(name))
    if result.secceeded:
        return 'versions/' + name
    else:
        return None
