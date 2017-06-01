import redis
pool = redis.ConnectionPool(host = 'localhost', port = 12345, db = 0)
conn = redis.StrictRedis(connection_pool = pool)
conn.slaveof('localhost', 6379)
