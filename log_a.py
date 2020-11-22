import logging
import time

logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format = '%(levelname)s  %(filename)s  line:%(lineno)d  [%(asctime)s] %(message)s',
    # time = str(time.strftime("%Y-%m-%d %X"))

    # format = time +' %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt = '%a, %d %b %Y %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    # filename = 'd:/report.log',
    # 打开日志文件的方式
    filemode = 'w'
)

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info('this is a log')
    logger.info('this is a log1')
