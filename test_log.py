import os
import time
import logging
from log import create_logger

from importlib import reload
reload(create_logger)

# # # 日志初始化# # 使用年-月-日作为生产文件夹的名，便于寻找# # 每一次执行这个文件的时候   直接给出统一的时间戳
# timeStamp = "online_" + str(time.strftime('%Y%m%d', time.localtime(time.time())))
# fileDir = "logs/" + timeStamp  # # 创建给出这次访问的日志# # 判断文件夹不存在
# if not os.path.exists(fileDir):
#     os.makedirs("logs/" + timeStamp)
#     fileLogName = "logs/" + timeStamp + "/online.log"

fileDir = "logs"
if not os.path.exists(fileDir):
    os.makedirs(fileDir)
fileLogName = fileDir + r'/app.log'
logger = create_logger.CreateLog('test', log_ouput_file=fileLogName).get_logger()

logger.info('aa')
logger.info('bb')
