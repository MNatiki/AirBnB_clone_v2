#!/usr/bin/env python3
"""
Write a Fabric script that generates a .tgz
"""

from fabric.api import *
from datetime import datetime
import os


@runs_once
def do_pack():
    """
    The function `do_pack()` creates a compressed archive file of the
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
