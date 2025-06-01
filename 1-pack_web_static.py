#!/usr/bin/python3
""" a fabric script to generate a .tgz archive from web_static folder"""
from fabric.api import local
from time import strftime
from os.path import exists, isdir
import os


def do_pack():
    """
    Generates a .tgz file from the contents of the web_static folder
    Returns:
        file path when successful or none otherwise.

    """
    
    date_time = strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(date_time)
    file_path = "version/{}".format(file_name)

    print("Packing web_static to {} web_static".format(file_path))
    result = local("tar -cvzf {} web_static".format(file_path))
    
    if result.failed:
        return none  

    return file_name
    except Exception as e:
        return None
