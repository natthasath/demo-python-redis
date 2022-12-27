import redis
r = redis.Redis(host='10.100.100.82', port=6379, db=0)
r.set('mailapp', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoibmF0dGhhc2F0aC5zYWtAbmlkYS5hYy50aCIsImV4cGlyZXMiOjE2NjA2Mzk4MTkuMzk4MzE4OH0.xDC2x7puCpKOLqR4y52h3Bm6dP0tWFhl9RQMwuzB64M')
print(r.get('mailapp'))