#!/usr/bin/env python3
""" Task 0 """
from redis import Redis
from typing import Union
from uuid import uuid4


class Cache:
    """ The class cache """

    def __init__(self):
        """ Init method for class Cache """
        self._redis = Redis()
        # Cleare the database from all keys.
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        A method store the input data in Redis using the random key

        Return: the random key.
        """
        random_key = uuid4()
        self._redis.set(str(random_key), data)

        return str(random_key)
