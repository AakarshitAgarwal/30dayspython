import json
import redis

redis_client = redis.Redis(host='localhost',port=6379,db=0)

username = redis_client.get('username')

print(username)

redis_client.set('fundamental_data',json.dumps({"aa":21}))