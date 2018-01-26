# -*- coding: utf-8 -*-

import sys, os, time
import  logging


logging.basicConfig(filename='logger.log', level=logging.INFO)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')



if __name__ == "__main__":
    print os.getcwd()