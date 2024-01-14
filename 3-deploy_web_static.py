#!/usr/bin/python3
"""Create and distributes an archive to web servers"""
from os.path import isdir
import os.path 
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ["52.201.190.48", "54.90.56.0"]


def do_pack():
    """generates a tgz archive"""
    try:
        date = time.strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    arichve_path = do_pack()
    if arichve_path is None:
        return False
    return do_deploy(arichve_path)
