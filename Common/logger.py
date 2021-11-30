# @Time :2021-11-19 11:47
# @Author :ShaylorLaw
# @File :logger.py

# import logging
# import time
# from Common import dir_config
#
# # logging.basicConfig(filename=dir_config.logs_dir+ \
# #                              '/logs.log',level=logging.INFO,filemode='w')
#
# logger=logging.getLogger()
# logger.setLevel(logging.INFO)
# rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
# log_name=dir_config.logs_dir+\
#         'logs.log'
# fh=logging.FileHandler(log_name,mode='w')
# fh.setLevel(logging.DEBUG)
# formatter=logging.Formatter("%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")
# fh.setFormatter(formatter)
# logger.addHandler(fh)
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
#
# logging.basicConfig(filename=dir_config.logs_dir+ \
#                              '/logs.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


import logging
import time
import os
from Common import dir_config


class Log(object):
    '''
封装后的logging
    '''

    def __init__(self, logger=None, log_cate='search'):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d")
        #file_dir = os.getcwd() + '/../log'
        file_dir = dir_config.logs_dir + \
            '/logs.log'
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        self.log_path = file_dir
        self.log_name = self.log_path + "/" + log_cate + "." + self.log_time + '.log'
        # print(self.log_name)

        fh = logging.FileHandler(self.log_name, 'a',encoding="UTF-8")  # 追加模式  这个是python2的
        # fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def getlog(self):
        return self.logger