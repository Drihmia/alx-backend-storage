#!/usr/bin/env python3
""" Task 0 """
import functools
import redis
from typing import Union, Callable, Optional
import uuid


def replay(string: Callable) -> None:
    """
    A method display the history of calls of a particular function.
    """
    redis_client = redis.Redis()
    name = string.__qualname__
    n_calls = redis_client.get(name).decode('utf-8')

    print(f"{name} was called {n_calls} times:")
    inputs_list = redis_client.lrange(f"{name}:inputs", 0, -1)
    outputs_list = redis_client.lrange(f"{name}:outputs", 0, -1)
    for i, j in zip(inputs_list, outputs_list):
        print(
            f"{name}(*{i.decode('utf-8')}) -> {j.decode('utf-8')}")


def count_calls(method: Callable) -> Callable:
    """
    A decorator that count how many times methods of the Cache class are called
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)  # line 19
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that ccreate input and output list keys, respectively.

    example:
    >>> lrange Cache.store:inputs 0 -1
        1) "(b'first',)"
        2) "(b'second',)"
        3) "(b'third',)"
    >>> lrange Cache.store:outputs 0 -1
        1) "36e383a2-9f82-4d86-b005-c3c8f57b8ec2"
        2) "7d73b286-c2b7-4c20-97e9-98309169ae0d"
        3) "faef27a5-253a-4514-9258-afa2539fc77e"
    """
    @functools.wraps(method)
    def wrapper(self, *args):
        """ wrapper """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args[0:2]))
        temp_ret = method(self, *args)  # line 40
        self._redis.rpush(f"{method.__qualname__}:outputs", str(temp_ret))
        return temp_ret
    return wrapper


class Cache:
    """ The class cache """

    def __init__(self):
        """ Init method for class Cache """
        self._redis = redis.Redis()

        # Cleare the database from all keys.
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self,
              data: Union[str, bytes, int, float]
              ) -> str:
        """
        A method store the input data in Redis using the random key

        Return: the random key.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    @count_calls
    @call_history
    def get(self,
            key: str,
            fn: Optional[Callable[[bytes],
                                  Union[str, int, float, bytes]]] = None
            ) -> Union[str, int, float, bytes, None]:
        """
        A method that gets back the data in Redis using provided key

        also it does convert the data from Redis using fn Callable

        Return: data
        """
        returned_key = self._redis.get(key)
        if returned_key is not None and fn is not None:
            return fn(returned_key)
        return returned_key

    @count_calls
    @call_history
    def get_str(self, key: str) -> Optional[str]:
        """ Special case of the method: get """

        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    @count_calls
    @call_history
    def get_int(self, key: str) -> Optional[int]:
        """ Special case of the method: get """

        return self.get(key, fn=int)
