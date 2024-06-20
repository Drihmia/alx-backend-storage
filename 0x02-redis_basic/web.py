#!/usr/bin/env python3
""" Task 5: Advanced task """
from functools import wraps
from redis import Redis
from requests import get
from typing import Callable


def decorator(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwargs):
        if (r.ttl(f"count:{args[-1]}")) == -2:
            r.setex(f"count:{args[-1]}", 10, 1)
        else:
            r.incrby(f"count:{args[-1]}", 1)
        print(r.get(f"count:{args[-1]}").decode('UTF-8'))
        return method(*args, **kwargs)
    return wrapper


@decorator
def get_page(url: str) -> str:
    """ Description """
    with get(url) as res:
        if res.status_code == 200:
            return res.content.decode('UTF-8')
        else:
            return ""


if __name__ == "__main__":
    r = Redis()
    base_url = "http://google.com"
    base_url = "http://slowwly.robertomurray.co.uk"
    content = get_page(base_url)
    # print(content[:10])
