import  logging



# 日志： DEBUG INFO WARN ERROR

# 灵活配置日志级别,日志格式,输出位置
logging.basicConfig(level=logging.WARN,  # 日志类型为DEBUG或者比DEBUG级别更高的类型保存在日志文件中;
                   format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                   datefmt='%a, %d %b %Y %H:%M:%S',
                   filename='lagou.log',
                   filemode='w')



logging.info('info')
# logging.warning('warn')
logging.error('error')