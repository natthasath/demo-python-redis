import redis
from decouple import config

r = redis.Redis(host=config("REDIS_HOST"), port=config("REDIS_PORT"), password=config("REDIS_PASS"), db=config("REDIS_DB"))
r.set('app', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoibmF0dGhhc2F0aC5zYWtAbmlkYS5hYy50aCIsImV4cGlyZXMiOjE2NjA2Mzk4MTkuMzk4MzE4OH0.xDC2x7puCpKOLqR4y52h3Bm6dP0tWFhl9RQMwuzB64M')
print(r.get('app'))