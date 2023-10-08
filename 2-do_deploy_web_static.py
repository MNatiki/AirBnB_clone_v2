#!/usr/bin/env python3
"""
Fabric script (basgged on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy:
"""

from fabric.api import *
from os.path import exists
env.hosts = ['54.164.28.87', '100.26.164.50']
env.user = 'ubuntu'


def do_deploy(archive_path):
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        no_ext = file_name.split('.')[0]
        path = '/data/web_static/releases/'
        new_path = path + no_ext
        run('mkdir -p {}{}'.format(new_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, new_path))
        run('rm /tmp/{}'.format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(new_path))
        return True
    except Exception:
        return False
