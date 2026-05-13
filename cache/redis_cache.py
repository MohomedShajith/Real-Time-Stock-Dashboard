import io
import redis
import pandas as pd
client = redis.Redis(host='localhost', port=6379)

def set_cache(key,data):
    json_string = data.to_json()
    client.set(key, json_string,ex=300)


def get_cache(key):
    result = client.get(key)
    if result is not None:
     return pd.read_json(io.StringIO(result.decode('utf-8')))
    else:
       return None
    
    
    
print("redis_cache loaded")