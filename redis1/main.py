from asyncore import read
import redis
redis_host = 'localhost'
redis_port = 6379


def redis_string():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)
        r.set("message","Hello World!")
        msg = r.get("message")
        print(msg)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    redis_string()