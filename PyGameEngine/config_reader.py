#!/usr/bin/env python3

#import ConfigParser
from pathlib import Path
from configparser import ConfigParser

##########################################
# Initialization of the config files.  
##########################################
def initConfig():
    init_main_config()
    init_key_config()

##########################################
# Initialization of the app config file.  
# Checks for the config file and 
# if it isn't there creates it.
##########################################
def init_main_config():
    fileName = './config/config.cfg'
    HERE = Path(__file__).parent.resolve()
    PATH = HERE / fileName
    if PATH.exists():
        print ('main config file found')
    else:
        print ('creating config file')
        config = ConfigParser()
        config['graphics'] = {
            'display_width':'800',
            'display_height':'600'
        }
        config['sound'] = {
            'volume':'10'
        }
        config['difficulty'] = {
            'difficulty':'hard'
        }
        config['logging'] = {
            'log_file':'system.log',
            'logging_dir':'./logs/',
            'log_level':'INFO',
            'logging_mode':'a'
        }
        with open(PATH, 'w') as configfile:
            config.write(configfile)


##########################################
# Initialization of the app config file.  
# Checks for the config file and 
# if it isn't there creates it.
##########################################
def init_key_config():
    fileName = './config/key_bind.cfg'
    HERE = Path(__file__).parent.resolve()
    PATH = HERE / fileName
    if PATH.exists():
        print ('key_bind config file found')
    else:
        print ('creating config file')
        config = ConfigParser()
        config['key_bindings'] = {
            'DELETE':'K_BACKSPACE',
            'ALT_DELETE':'K_DELETE',
            'CAMERA_UP':'K_UP',
            'CAMERA_DOWN':'K_DOWN',
            'CAMERA_RIGHT':'K_RIGHT',
            'CAMERA_LEFT':'K_LEFT',
            'TEST_SPAWN_RIGHT':'K_f',
            'TEST_SPAWN_DOWN':'K_d',
            'MENU':'K_ESCAPE',
#           unnasigend keys
            'UNNASIGEND_K_TAB':'K_TAB',
            'UNNASIGEND_K_CLEAR':'K_CLEAR',
            'UNNASIGEND_K_RETURN':'K_RETURN',
            'UNNASIGEND_K_PAUSE':'K_PAUSE',
            'UNNASIGEND_K_SPACE':'K_SPACE',
            'UNNASIGEND_K_EXCLAIM':'K_EXCLAIM',
            'UNNASIGEND_K_QUOTEDBL':'K_QUOTEDBL',
            'UNNASIGEND_K_HASH':'K_HASH',
            'UNNASIGEND_K_DOLLAR':'K_DOLLAR',
            'UNNASIGEND_K_AMPERSAND':'K_AMPERSAND',
            'UNNASIGEND_K_QUOTE':'K_QUOTE',
            'UNNASIGEND_K_LEFTPAREN':'K_LEFTPAREN',
            'UNNASIGEND_K_RIGHTPAREN':'K_RIGHTPAREN',
            'UNNASIGEND_K_ASTERISK':'K_ASTERISK',
            'UNNASIGEND_K_PLUS':'K_PLUS',
            'UNNASIGEND_K_COMMA':'K_COMMA',
            'UNNASIGEND_K_MINUS':'K_MINUS',
            'UNNASIGEND_K_PERIOD':'K_PERIOD',
            'UNNASIGEND_K_SLASH':'K_SLASH',
            'UNNASIGEND_K_0':'K_0',
            'UNNASIGEND_K_1':'K_1',
            'UNNASIGEND_K_2':'K_2',
            'UNNASIGEND_K_3':'K_3',
            'UNNASIGEND_K_4':'K_4',
            'UNNASIGEND_K_5':'K_5',
            'UNNASIGEND_K_6':'K_6',
            'UNNASIGEND_K_7':'K_7',
            'UNNASIGEND_K_8':'K_8',
            'UNNASIGEND_K_9':'K_9',
            'UNNASIGEND_K_COLON':'K_COLON',
            'UNNASIGEND_K_SEMICOLON':'K_SEMICOLON',
            'UNNASIGEND_K_LESS':'K_LESS',
            'UNNASIGEND_K_EQUALS':'K_EQUALS',
            'UNNASIGEND_K_GREATER':'K_GREATER',
            'UNNASIGEND_K_QUESTION':'K_QUESTION',
            'UNNASIGEND_K_AT':'K_AT',
            'UNNASIGEND_K_LEFTBRACKET':'K_LEFTBRACKET',
            'UNNASIGEND_K_BACKSLASH':'K_BACKSLASH',
            'UNNASIGEND_K_RIGHTBRACKET':'K_RIGHTBRACKET',
            'UNNASIGEND_K_CARET':'K_CARET',
            'UNNASIGEND_K_UNDERSCORE':'K_UNDERSCORE',
            'UNNASIGEND_K_BACKQUOTE':'K_BACKQUOTE',
            'UNNASIGEND_K_a':'K_a',
            'UNNASIGEND_K_b':'K_b',
            'UNNASIGEND_K_c':'K_c',
            'UNNASIGEND_K_e':'K_e',
            'UNNASIGEND_K_g':'K_g',
            'UNNASIGEND_K_h':'K_h',
            'UNNASIGEND_K_i':'K_i',
            'UNNASIGEND_K_j':'K_j',
            'UNNASIGEND_K_k':'K_k',
            'UNNASIGEND_K_l':'K_l',
            'UNNASIGEND_K_m':'K_m',
            'UNNASIGEND_K_n':'K_n',
            'UNNASIGEND_K_o':'K_o',
            'UNNASIGEND_K_p':'K_p',
            'UNNASIGEND_K_q':'K_q',
            'UNNASIGEND_K_r':'K_r',
            'UNNASIGEND_K_s':'K_s',
            'UNNASIGEND_K_t':'K_t',
            'UNNASIGEND_K_u':'K_u',
            'UNNASIGEND_K_v':'K_v',
            'UNNASIGEND_K_w':'K_w',
            'UNNASIGEND_K_x':'K_x',
            'UNNASIGEND_K_y':'K_y',
            'UNNASIGEND_K_z':'K_z',
            'UNNASIGEND_K_KP0':'K_KP0',
            'UNNASIGEND_K_KP1':'K_KP1',
            'UNNASIGEND_K_KP2':'K_KP2',
            'UNNASIGEND_K_KP3':'K_KP3',
            'UNNASIGEND_K_KP4':'K_KP4',
            'UNNASIGEND_K_KP5':'K_KP5',
            'UNNASIGEND_K_KP6':'K_KP6',
            'UNNASIGEND_K_KP7':'K_KP7',
            'UNNASIGEND_K_KP8':'K_KP8',
            'UNNASIGEND_K_KP9':'K_KP9',
            'UNNASIGEND_K_KP_PERIOD':'K_KP_PERIOD',
            'UNNASIGEND_K_KP_DIVIDE':'K_KP_DIVIDE',
            'UNNASIGEND_K_KP_MULTIPLY':'K_KP_MULTIPLY',
            'UNNASIGEND_K_KP_MINUS':'K_KP_MINUS',
            'UNNASIGEND_K_KP_PLUS':'K_KP_PLUS',
            'UNNASIGEND_K_KP_ENTER':'K_KP_ENTER',
            'UNNASIGEND_K_KP_EQUALS':'K_KP_EQUALS',
            'UNNASIGEND_K_INSERT':'K_INSERT',
            'UNNASIGEND_K_HOME':'K_HOME',
            'UNNASIGEND_K_END':'K_END',
            'UNNASIGEND_K_PAGEUP':'K_PAGEUP',
            'UNNASIGEND_K_PAGEDOWN':'K_PAGEDOWN',
            'UNNASIGEND_K_F1':'K_F1',
            'UNNASIGEND_K_F2':'K_F2',
            'UNNASIGEND_K_F3':'K_F3',
            'UNNASIGEND_K_F4':'K_F4',
            'UNNASIGEND_K_F5':'K_F5',
            'UNNASIGEND_K_F6':'K_F6',
            'UNNASIGEND_K_F7':'K_F7',
            'UNNASIGEND_K_F8':'K_F8',
            'UNNASIGEND_K_F9':'K_F9',
            'UNNASIGEND_K_F10':'K_F10',
            'UNNASIGEND_K_F11':'K_F11',
            'UNNASIGEND_K_F12':'K_F12',
            'UNNASIGEND_K_F13':'K_F13',
            'UNNASIGEND_K_F14':'K_F14',
            'UNNASIGEND_K_F15':'K_F15',
            'UNNASIGEND_K_NUMLOCK':'K_NUMLOCK',
            'UNNASIGEND_K_CAPSLOCK':'K_CAPSLOCK',
            'UNNASIGEND_K_SCROLLOCK':'K_SCROLLOCK',
            'UNNASIGEND_K_RSHIFT':'K_RSHIFT',
            'UNNASIGEND_K_LSHIFT':'K_LSHIFT',
            'UNNASIGEND_K_RCTRL':'K_RCTRL',
            'UNNASIGEND_K_LCTRL':'K_LCTRL',
            'UNNASIGEND_K_RALT':'K_RALT',
            'UNNASIGEND_K_LALT':'K_LALT',
            'UNNASIGEND_K_RMETA':'K_RMETA',
            'UNNASIGEND_K_LMETA':'K_LMETA',
            'UNNASIGEND_K_LSUPER':'K_LSUPER',
            'UNNASIGEND_K_RSUPER':'K_RSUPER',
            'UNNASIGEND_K_MODE':'K_MODE',
            'UNNASIGEND_K_HELP':'K_HELP',
            'UNNASIGEND_K_PRINT':'K_PRINT',
            'UNNASIGEND_K_SYSREQ':'K_SYSREQ',
            'UNNASIGEND_K_BREAK':'K_BREAK',
            'UNNASIGEND_K_MENU':'K_MENU',
            'UNNASIGEND_K_POWER':'K_POWER',
            'UNNASIGEND_K_EURO':'K_EURO'
        }
        with open(PATH, 'w') as configfile:
            config.write(configfile)

##########################################
# Reads a value from the config file.
# sectionName is the name of the section in the file
# tag is the key of the config value
# typeVal is the type (string, int, float, bool) of the value
##########################################    
def read_config(config_file, section_name, tag, typeVal):
    file_name = './config/'+config_file+'.cfg'
    parser = ConfigParser()
    parser.read(file_name)
    if typeVal== 'int':
        configValue = parser.getint(section_name, tag)
    elif typeVal== 'string':
        configValue = parser.get(section_name, tag)
    elif typeVal== 'bool':
        configValue = parser.getboolean(section_name, tag)
    elif typeVal== 'float':
        configValue = parser.getfloat(section_name, tag)
    print ("config values read", tag, ':', configValue)
    # logging.debug("config values read %s", configValue)
    return configValue


##########################################
# changes a value in the config file from the game settings
# sectionName the name of the section
# tag is the key that you are changing to value for
# value is the new value to set
##########################################
def changeSetting(config_file, sectionName, tag, value):
    fileName = './config/'+config_file+'.cfg'
    config = ConfigParser()
    config.set(sectionName, tag, value)
    logging.debug("config values read %s, %s, %s", sectionName, tag, value)
    with open(fileName, 'wb') as configfile:
        config.write(configfile)
