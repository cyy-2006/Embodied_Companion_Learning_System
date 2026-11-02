import redis
import inspect

redis_client_args = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 0,
    "decode_responses": True,
}

if "protocol" in inspect.signature(redis.Redis.__init__).parameters:
    # redis-py 4+ uses `protocol`
    redis_client_args["protocol"] = 2
else:
    # redis-py 3.x style
    redis_client_args["protocol_version"] = 2

redis_client = redis.Redis(**redis_client_args)

target_url = r'http://10.121.113.158:3000/uploads\71aea4cdf2664108a7621c1704cb1d01.mp4'
redis_client.lrem('dsavd:user:videos:admin', 0, target_url)
print("删除成功")
