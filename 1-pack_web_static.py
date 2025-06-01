#!/usr/bin/python3
<<<<<<< HEAD
"""Fabric script to generate a .tgz archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to generate a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.succeeded:
        return file_name
    return None
=======
"""
Fabric script to genereate tgz archive
using: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
>>>>>>> e94de2ba8dde146dfd8f2e393ffdd796b0811696
