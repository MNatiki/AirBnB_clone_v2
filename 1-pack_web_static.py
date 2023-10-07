#!/usr/bin/env python3
"""
Write a Fabric script that generates a .tgz
archive from the contents of the web_static,
using the function do_pack.
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
    now = datetime.now()
    name = "web_static_" + str(now.year) + str(now.month) + \
        str(now.day) + str(now.hour) + str(now.minute) + \
        str(now.second) + ".tgz"

    if not os.path.exists("versions"):
        os.makedirs("versions")

    print("Packing web_static to versions/{}".format(name))
    result = local("tar -cvzf versions/{} web_static".format(name))

    if result.succeeded:
        return 'versions/' + name
    else:
        return None
