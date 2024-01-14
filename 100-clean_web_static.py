#!/usr/bin/python3
""" Fabfile to delete out-of-date archives. """
from fabric.api import *

env.hosts = ["52.201.190.48", "54.90.56.0"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    if int(number) == 0:
        number = 1
    number = int(number) + 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
