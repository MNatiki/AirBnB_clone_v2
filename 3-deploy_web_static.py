#!/usr/bin/python3
"""
The `deploy` function creates a compressed archive file of the
"""
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['54.164.28.87', '100.26.164.50']


def deploy():
    """
    The function "deploy" calls the "do_pack" function and
    """
    my_path = do_pack()
    # print(os.path.exists(my_path))
    if my_path:
        my_dep = do_deploy(my_path)
        return my_dep
    return my_path
