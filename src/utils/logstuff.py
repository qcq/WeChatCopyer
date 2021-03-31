# -*- coding:utf-8 -*-
#!/usr/bin/env python3

'''
create decorator for logging
features:
1. create log when enter the function
2. create log when out the function
'''

from functools import wraps


def log_the_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before it do
        result = func(*args, **kwargs)
        # after func call, do something
        return result
    return wrapper
