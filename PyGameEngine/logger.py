#!/usr/bin/env python3

# Most of this code was not mine but was from
# https://www.programcreek.com/python/example/136/logging.basicConfig

import logging

###################################
# Initialize the logging.
# logFile is the name of the logfile
# logLevel is the logging level (INFO,DEBUG,ERROR)
# loggingMode is the logging mode(a for append, w for overwrite)
###################################

def initLogging(log_file, log_dir, log_level, logging_mode):
    logging.basicConfig(filename=log_dir+log_file,
                            filemode=logging_mode,
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=log_level)
    logging.info("_______________________NEW RUN_______________________")
    logging.info("Logger Initalized at level %s", log_level)
