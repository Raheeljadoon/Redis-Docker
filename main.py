import redis
import json
from datetime import timedelta

redis_host = 'localhost'
redis_port = 6379

"""---------------------- these are test basic ftn---------------------"""


def redis_string():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)

        r.set("message", "hello world testing")
        r.set("test", "hello world testing new")

        test = r.get('test')
        msg = r.get("message")

        print(test)
        print(msg)

    except:
        print("something went wrong")


def redis_int():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)

        r.set("integer", 100)
        o_num = r.get("integer")
        print("original number is :", o_num)

        r.incr("integer")
        after_incre = r.get("integer")
        print("after increment :", after_incre)

        all_keys = r.keys("*")
        print("All Keys Stored in Db :", all_keys)

    except:
        print("Something Went Wrong")

        """======----- practise basic ftn over ----------------"""


"""---------------------- this ftn is for cache storage---------------------"""


def cache_test():

    try:
        r = redis.Redis(host=redis_host, port=redis_port, db=0)
        cache_test = r.get("cache_test")

        if cache_test == None:

            r.set("cache_test", json.dumps(
                {"user": "raheel", "password": 1234, "email": "raheel@gmail.com"}))
            print("setting cache_test now ")
            r.expire("cache_test", timedelta(seconds=60))

            data = input("please enter the record :")
        else:
            print("already present in db cache")
            print("Now value will be coming from cache----\nDetail of user Raheel are :",
                  json.loads(cache_test))

    except:
        print("Something Went Wrong")


if __name__ == '__main__':
    redis_string()
    redis_int()
    cache_test()
