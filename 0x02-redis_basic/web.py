#!/usr/bin/env python3
""" Task 5: Advanced task """
import functools
import redis
import requests
from typing import Callable

r = redis.Redis()


def decorator(method: Callable) -> Callable:
    """ decorator Description """
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """ wrapper Description """
        r.incr(f"count:{url}")
        return method(url)
    return wrapper


@decorator
def get_page(url: str) -> str:
    """ Description """
    cached_content = r.get(f"cache:{url}")
    if cached_content:
        return cached_content.decode('utf-8')

    with requests.get(url) as res:
        content = res.text
        r.setex(f"cache:{url}", 10, str(content))
        return content
