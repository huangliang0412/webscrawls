#!/usr/bin/env python3
import redis
pool = redis.ConnectionPool(host = 'localhost', port = 6379, db = 0)
conn = redis.StrictRedis(connection_pool = pool)

