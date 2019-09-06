import redis


try:
    r = redis.StrictRedis(host='172.25.254.123', port=6379)
except Exception as e:
    print(e)
else:
    r.set("name", "fentiao")
    print(r.get("name"))


