#!/usr/bin/env python3

import os
from logger import logging

def init_dirs():
    make_dir('config')
    make_dir('factions')
    make_dir('logs')


def make_dir(dir_name):
    try:
        os.makedirs(dir_name)
    except FileExistsError:
        logging.error("Error createing directory %s", dir_name)
        pass