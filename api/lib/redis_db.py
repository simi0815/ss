import redis
from api.conf.api_config import REDIS_IP, REDIS_PORT


class RedisDB():
    def __init__(self):
        self.red = redis.Redis(host=REDIS_IP, port=REDIS_PORT, db=0)
    def set(self,key,value):
        self.red.set('name', 'zhangsan')

  # 添加

print(r.get('name'))
