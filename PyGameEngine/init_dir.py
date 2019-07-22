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
        logging.info("Directory %s already exists", dir_name)
        pass