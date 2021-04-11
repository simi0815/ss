import redis

# from api.conf.api_config import REDIS_IP, REDIS_PORT
REDIS_IP = '127.0.0.1'
REDIS_PORT = 6379


class RedisDB():
    def __init__(self):
        self.red = redis.Redis(host=REDIS_IP, port=REDIS_PORT, db=0, decode_responses=True)

    def set(self, key, hash):
        self.red.hset(key, mapping=hash)

    def set_one(self, key, one_name, one_value):
        self.red.hset(key, one_name, one_value)

    def get(self, key):
        return self.red.hgetall(key)


if __name__ == '__main__':
    rd = RedisDB()

    rd.set_one("h2","age","19")
    print(rd.get("h2"))
