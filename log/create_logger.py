import logging
from logging.handlers import TimedRotatingFileHandler

SRC_IP = 'aa'


class CreateLog():
    def __init__(self, name, level=logging.DEBUG, log_ouput_file=None):
        self.logger = logging.getLogger(name)
        self.src_ip = SRC_IP
        self.logger.setLevel(level)

        format1 = '[' + self.src_ip + ']%(asctime)s-%(funcName)s %(lineno)d[%(levelname)s] %(message)s'
        rf_handler = logging.StreamHandler()  # 输出到屏幕屏幕
        rf_handler.setFormatter(logging.Formatter(format1))
        self.logger.addHandler(rf_handler)
        if log_ouput_file:  # 输出到文件
            f_handler = TimedRotatingFileHandler(
                filename=log_ouput_file, when="midnight", interval=1, backupCount=0)  # midnight:凌晨滚动
            # f_handler.suffix = "%Y%m%d%H%M%S.log"
            f_handler.setFormatter(logging.Formatter(format1))
            self.logger.addHandler(f_handler)

    def get_logger(self):
        return self.logger
