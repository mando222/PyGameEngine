#!/usr/bin/env python3

from config_reader import *

class key_bindings:
    def __init__(self):
        self.DELETE = read_config('key_bind', 'key_bindings', 'delete', 'string')
        self.ALT_DELETE = read_config('key_bind', 'key_bindings', 'alt_delete', 'string')
        self.CAMERA_UP = read_config('key_bind', 'key_bindings', 'camera_up', 'string')
        self.CAMERA_DOWN = read_config('key_bind', 'key_bindings', 'camera_down', 'string')
        self.CAMERA_RIGHT = read_config('key_bind', 'key_bindings', 'camera_right', 'string')
        self.CAMERA_LEFT = read_config('key_bind', 'key_bindings', 'camera_left', 'string')
        self.TEST_SPAWN_RIGHT = read_config('key_bind', 'key_bindings', 'test_spawn_right', 'string')
        self.TEST_SPAWN_DOWN = read_config('key_bind', 'key_bindings', 'test_spawn_down', 'string')
        self.MENU = read_config('key_bind', 'key_bindings', 'menu', 'string')
        