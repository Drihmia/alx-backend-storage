#!/usr/bin/env python3
""" Task 5: Advanced task """
import functools
import redis
import requests
from typing import Callable


def decorator(method: Callable) -> Callable:
    """ decorator Description """
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        """ wrapper Description """
        if (r.ttl(f"count:{args[-1]}")) == -2:
            r.setex(f"count:{args[-1]}", 10, 1)
        else:
            r.incrby(f"count:{args[-1]}", 1)
        # print(r.get(f"count:{args[-1]}").decode('UTF-8'))
        return method(*args, **kwargs)
    return wrapper


@decorator
def get_page(url: str) -> str:
    """ Description """
    with requests.get(url) as res:
        if res.status_code == 200:
            return res.text
        else:
            return ""


if __name__ == "__main__":
    r = redis.Redis()
    base_url = "http://slowwly.robertomurray.co.uk"
    base_url = "http://google.com"
    content = get_page(base_url)
    # print(content[:10])
