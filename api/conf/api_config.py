from searchsystem.settings import STATICFILES_DIRS

# 231服务器静态文件目录
# STATIC_ROOT = "/var/searchsystem/dist/xml"
# 本地静态文件目录配置
STATIC_ROOT = STATICFILES_DIRS[0]
# es服务器集群ip地址和端口号配置
ES_IP_ADDRESSS = ['192.168.1.230:9200']
# mongodb ip地址和端口号
MONGO_ADDRESS = '192.168.1.231'
MONGO_PORT = 27017
# redis IP地址
REDIS_IP = '192.168.1.231'
# redis port 地址
REDIS_PORT = 6379
# 当前的通讯协议和ip地址或域名
PROTOCOL_IP_OR_DOMAIN = "http://192.168.8.35:8000"
# #231服务器的ip地址和域名
# PROTOCOL_IP_OR_DOMAIN = "http://192.168.1.231"
# 外网访问的静态文件地址前缀
STATIC_URL = "/xml"
# mongodb中一个集合取得条数
MONGO_ONE_LIMIT = 10
# es数据库索引取得条数
ES_ONE_LIMIT = 5
