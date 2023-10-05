#!/usr/bin/python3
"""
The `do_pack()` function creates a compressed archive file of the
`web_static` folder and saves it in the `versions` directory
"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['54.90.60.221:80', '52.201.220.122:80']


# def do_pack():
#     """
#     The function `do_pack()` creates a compressed archive file of the
#     `web_static` folder and saves it in the `versions` directory, and
#     then prints the path and size of the created archive file.
#     """
#     today = datetime.now()
#     name = "web_static_" + str(today.year) + str(today.month) + \
#         str(today.day) + str(today.hour) + str(today.minute) + \
#         str(today.second) + ".tgz"
#     local("mkdir -p versions")
#     local(f'tar -cvzf versions/{name}.tgz web_static')
#     # print(name)
#     try:
#         print("web_static packed: versions/{} -> \
#               {os.get.path.getsize(os.getcwd() + '/versions/'
#    + name)}Bytes".format(name))
#     except Exception:
#         return None
#     return '/versions/' + name


def do_deploy(archive_path):
    if os.path.exists(archive_path) is False:
        print("not a path")
        return False
    put(archive_path, '/tmp/')
    myfile = archive_path.split('/')[-1]
    myfile1 = myfile.split('.')[0]
    path = "/data/web_static/releases/"
    run("mkdir -p {}{}}/".format(path, myfile1))
    run("tar -xzf /tmp/{} -C {}{}/".format(myfile, path, myfile1))
    run("rm /tmp/{}".format(myfile))
    run("{}{}/web_static/* {}/".format(path, myfile1, myfile1))
    run("rm -rf {}/{}/web_static".format(path, myfile1))
    run("rm -rf /data/web_static/current")
    run("ln -s {}{}/ /data/web_static/current".format(path, myfile1))

