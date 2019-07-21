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
        print ('config file found')
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
        print ('config file found')
    else:
        print ('creating config file')
        config = ConfigParser()
        config['key_bindings'] = {
            'K_BACKSPACE':'K_BACKSPACE',
            'K_TAB':'K_TAB',
            'K_CLEAR':'K_CLEAR',
            'K_RETURN':'K_RETURN',
            'K_PAUSE':'K_PAUSE',
            'K_ESCAPE':'K_ESCAPE',
            'K_SPACE':'K_SPACE',
            'K_EXCLAIM':'K_EXCLAIM',
            'K_QUOTEDBL':'K_QUOTEDBL',
            'K_HASH':'K_HASH',
            'K_DOLLAR':'K_DOLLAR',
            'K_AMPERSAND':'K_AMPERSAND',
            'K_QUOTE':'K_QUOTE',
            'K_LEFTPAREN':'K_LEFTPAREN',
            'K_RIGHTPAREN':'K_RIGHTPAREN',
            'K_ASTERISK':'K_ASTERISK',
            'K_PLUS':'K_PLUS',
            'K_COMMA':'K_COMMA',
            'K_MINUS':'K_MINUS',
            'K_PERIOD':'K_PERIOD',
            'K_SLASH':'K_SLASH',
            'K_0':'K_0',
            'K_1':'K_1',
            'K_2':'K_2',
            'K_3':'K_3',
            'K_4':'K_4',
            'K_5':'K_5',
            'K_6':'K_6',
            'K_7':'K_7',
            'K_8':'K_8',
            'K_9':'K_9',
            'K_COLON':'K_COLON',
            'K_SEMICOLON':'K_SEMICOLON',
            'K_LESS':'K_LESS',
            'K_EQUALS':'K_EQUALS',
            'K_GREATER':'K_GREATER',
            'K_QUESTION':'K_QUESTION',
            'K_AT':'K_AT',
            'K_LEFTBRACKET':'K_LEFTBRACKET',
            'K_BACKSLASH':'K_BACKSLASH',
            'K_RIGHTBRACKET':'K_RIGHTBRACKET',
            'K_CARET':'K_CARET',
            'K_UNDERSCORE':'K_UNDERSCORE',
            'K_BACKQUOTE':'K_BACKQUOTE',
            'K_a':'K_a',
            'K_b':'K_b',
            'K_c':'K_c',
            'K_d':'K_d',
            'K_e':'K_e',
            'K_f':'K_f',
            'K_g':'K_g',
            'K_h':'K_h',
            'K_i':'K_i',
            'K_j':'K_j',
            'K_k':'K_k',
            'K_l':'K_l',
            'K_m':'K_m',
            'K_n':'K_n',
            'K_o':'K_o',
            'K_p':'K_p',
            'K_q':'K_q',
            'K_r':'K_r',
            'K_s':'K_s',
            'K_t':'K_t',
            'K_u':'K_u',
            'K_v':'K_v',
            'K_w':'K_w',
            'K_x':'K_x',
            'K_y':'K_y',
            'K_z':'K_z',
            'K_DELETE':'K_DELETE',
            'K_KP0':'K_KP0',
            'K_KP1':'K_KP1',
            'K_KP2':'K_KP2',
            'K_KP3':'K_KP3',
            'K_KP4':'K_KP4',
            'K_KP5':'K_KP5',
            'K_KP6':'K_KP6',
            'K_KP7':'K_KP7',
            'K_KP8':'K_KP8',
            'K_KP9':'K_KP9',
            'K_KP_PERIOD':'K_KP_PERIOD',
            'K_KP_DIVIDE':'K_KP_DIVIDE',
            'K_KP_MULTIPLY':'K_KP_MULTIPLY',
            'K_KP_MINUS':'K_KP_MINUS',
            'K_KP_PLUS':'K_KP_PLUS',
            'K_KP_ENTER':'K_KP_ENTER',
            'K_KP_EQUALS':'K_KP_EQUALS',
            'K_UP':'K_UP',
            'K_DOWN':'K_DOWN',
            'K_RIGHT':'K_RIGHT',
            'K_LEFT':'K_LEFT',
            'K_INSERT':'K_INSERT',
            'K_HOME':'K_HOME',
            'K_END':'K_END',
            'K_PAGEUP':'K_PAGEUP',
            'K_PAGEDOWN':'K_PAGEDOWN',
            'K_F1':'K_F1',
            'K_F2':'K_F2',
            'K_F3':'K_F3',
            'K_F4':'K_F4',
            'K_F5':'K_F5',
            'K_F6':'K_F6',
            'K_F7':'K_F7',
            'K_F8':'K_F8',
            'K_F9':'K_F9',
            'K_F10':'K_F10',
            'K_F11':'K_F11',
            'K_F12':'K_F12',
            'K_F13':'K_F13',
            'K_F14':'K_F14',
            'K_F15':'K_F15',
            'K_NUMLOCK':'K_NUMLOCK',
            'K_CAPSLOCK':'K_CAPSLOCK',
            'K_SCROLLOCK':'K_SCROLLOCK',
            'K_RSHIFT':'K_RSHIFT',
            'K_LSHIFT':'K_LSHIFT',
            'K_RCTRL':'K_RCTRL',
            'K_LCTRL':'K_LCTRL',
            'K_RALT':'K_RALT',
            'K_LALT':'K_LALT',
            'K_RMETA':'K_RMETA',
            'K_LMETA':'K_LMETA',
            'K_LSUPER':'K_LSUPER',
            'K_RSUPER':'K_RSUPER',
            'K_MODE':'K_MODE',
            'K_HELP':'K_HELP',
            'K_PRINT':'K_PRINT',
            'K_SYSREQ':'K_SYSREQ',
            'K_BREAK':'K_BREAK',
            'K_MENU':'K_MENU',
            'K_POWER':'K_POWER',
            'K_EURO':'K_EURO'
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
    print(file_name)
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
    print ("config values read %s", configValue)
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
