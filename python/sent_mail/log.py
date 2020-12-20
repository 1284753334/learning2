# coding=utf-8
from fishbase.fish_logger import *
from fishbase.fish_file import *


class Logger:
    def __init__(self, log_file_name='mail.log'):
        logpath = os.path.join(os.getcwd(), "log")
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        log_abs_filename = get_abs_filename_with_sub_path('log', log_file_name)[1]
        set_log_file(log_abs_filename)

    def info(self, log, if_print=False):
        logger.info(log)
        if if_print:print(log)

    def warn(self, log, if_print=False):
        logger.warn(log)
        if if_print: print(log)

    def error(self, log, if_print=False):
        logger.error(log)
        if if_print: print(log)
