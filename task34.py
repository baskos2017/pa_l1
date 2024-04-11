import time
import functools

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time  = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time, func.__name__
    return wrapper

@timer_decorator
def fibonacci_lru10(index):
    @functools.lru_cache(maxsize=10)
    def fibonacci_1(ind):
        if ind < 2:
            return ind
        return fibonacci_1(ind - 1) + fibonacci_1(ind - 2)

    result_list = [fibonacci_1(i) for i in range(index + 1)]
    return result_list

@timer_decorator
def fibonacci_lru16(index):
    @functools.lru_cache(maxsize=16)
    def fibonacci_1(ind):
        if ind < 2:
            return ind
        return fibonacci_1(ind - 1) + fibonacci_1(ind - 2)

    result_list = [fibonacci_1(i) for i in range(index + 1)]
    return result_list

@timer_decorator
def fibonacci_lru_none(index):
    @functools.lru_cache(maxsize=None)
    def fibonacci_1(ind):
        if ind < 2:
            return ind
        return fibonacci_1(ind - 1) + fibonacci_1(ind - 2)

    result_list = [fibonacci_1(i) for i in range(index + 1)]
    return result_list

@timer_decorator
def fibonacci(index):
    def fibonacci_1(ind):
        if ind < 2:
            return ind
        return fibonacci_1(ind - 1) + fibonacci_1(ind - 2)

    result_list = [fibonacci_1(i) for i in range(index + 1)]
    return result_list

print(fibonacci_lru10(25))


print(fibonacci_lru16(25))


print(fibonacci_lru_none(25))


print(fibonacci(25))