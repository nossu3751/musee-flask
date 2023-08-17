from redis import Redis

class RedisWrapper:
    def __init__(self):
        self.redis = None
    def init(self, host, port, decode_responses):
        self.redis = Redis(host=host, port=port, decode_responses=decode_responses)

redis_wrapper = RedisWrapper()