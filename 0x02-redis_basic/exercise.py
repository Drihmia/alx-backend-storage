#!/usr/bin/env python3
""" Task 0 """
from functools import wraps
from redis import Redis
from typing import Union, Callable, TypeVar, Any, Optional
from uuid import uuid4


T = TypeVar('T')


def count_calls(method: Callable) -> Callable:
    """
    A decorator that count how many times methods of the Cache class are called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incrby(method.__qualname__, 1)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ The class cache """

    def __init__(self):
        """ Init method for class Cache """
        self._redis = Redis()
        # Cleare the database from all keys.
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        A method store the input data in Redis using the random key

        Return: the random key.
        """
        random_key = uuid4()
        self._redis.set(str(random_key), data)

        # trigger the background save.
        # self._redis.bgsave()

        return str(random_key)

    @count_calls
    def get(self, key: str, fn: Callable[[Any], T] = None) -> Optional[T]:
        """
        A method that gets back the data in Redis using provided key

        also it does convert the data from Redis using fn Callable

        Return: data
        """
        returned_key = self._redis.get(key)
        if fn is not None and returned_key:
            returned_key = fn(returned_key)
        return returned_key

    @count_calls
    def get_str(self, key: str) -> Optional[str]:
        """ Special case of the method: get """

        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    @count_calls
    def get_int(self, key: str) -> Optional[int]:
        """ Special case of the method: get """

        return self.get(key, fn=int)
