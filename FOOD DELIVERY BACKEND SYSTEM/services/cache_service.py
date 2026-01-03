import redis
import json

r = redis.Redis(host = "redis", port = 6379, decode_responses=True)
def cache_set (key, value, ttl =300):
    r.setex(key, ttl, json.dumps(value))

def cache_get(key):
    data = r.get(key)
    return json.loads(data) if data else None