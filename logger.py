#! /usr/bin/env python
# coding=utf-8
import os
import logging
from logging.config import fileConfig


class Logger:
    # def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
    #     self.logger = logging.getLogger(path)
    #     self.logger.setLevel(logging.DEBUG)
    #     fmt = logging.Formatter(
    #         '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    #     # 设置控制台日志
    #     sh = logging.StreamHandler()
    #     sh.setFormatter(fmt)
    #     sh.setLevel(clevel)
    #     # 设置文件日志
    #     fh = logging.FileHandler(path)
    #     fh.setFormatter(fmt)
    #     fh.setLevel(Flevel)
    #     self.logger.addHandler(sh)
    #     self.logger.addHandler(fh)

    def __init__(self):
        fileConfig('logger.conf')
        self.logger = logging.getLogger()

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# if __name__ == '__main__':
#     logger = Logger()
#     for num in range(0, 100000):
#         logger.debug("一个debug信息{}".format(num))
#         logger.info("一个info信息{}".format(num))
#         logger.warn("一个warning信息{}".format(num))
#         logger.error("一个error信息{}".format(num))
#         logger.critical("一个critical信息{}".format(num))
