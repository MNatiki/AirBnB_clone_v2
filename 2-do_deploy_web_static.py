#!/usr/bin/env python3
"""
script that distributes an archive to your web servers.
"""

from fabric.api import *
from os.path import exists
import os

env.hosts = ['54.164.28.87', '100.26.164.50']
env.user = 'ubuntu'


def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to the /data/web_static/releases/ directory
        archive_filename = os.path.basename(archive_path)
        archive_no_extension = archive_filename.split(".")[0]
        release_folder = "/data/web_static/releases/"

        run("mkdir -p {}{}".format(release_folder, archive_no_extension))
        run("tar -xzf /tmp/{} -C {}{}".format(archive_filename, release_folder, archive_no_extension))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move the contents of the release folder to the proper location
        run("mv {0}{1}/web_static/* {0}{1}/".format(release_folder, archive_no_extension))

        # Remove the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {}{} /data/web_static/current".format(release_folder, archive_no_extension))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False

