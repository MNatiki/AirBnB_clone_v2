#!/usr/bin/python3
"""
The `deploy` function creates a compressed archive file of the
`web_static` folder and saves it in the `versions` for deployment
"""
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['52.201.220.122', '54.90.60.221']
my_path = do_pack()


def deploy():
    """
    The function "deploy" calls the "do_pack" function and
    if it returns a valid path, it calls the "do_deploy"
    function with that path and returns the result.
    """
    # print(os.path.exists(my_path))
    if my_path:
        my_dep = do_deploy(my_path)
        return my_dep
    return my_path
