#!/usr/bin/python3
"""Deploy web static to different servers"""
import re
from fabric.context_managers import cd
from fabric.api import env, put, run, sudo
from os.path import join, exists, splitext


env.user = "ubuntu"
env.hosts = ["54.242.215.110", "34.229.154.33"]
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Deploy a compressed archive to a remote server.
    Args:
        archive_path (str): The path to the compressed archive.
    Returns:
        bool: True if the deployment is successful, False otherwise.
    """
