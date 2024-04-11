import time


def my_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання '{func.__name__}': {end_time - start_time} секунд")
        return result
    return wrapper

@my_time
def my_func(digit1, digit2):
    for num in range(digit2 - digit1):
        print(num)

my_func(1, 100)
my_func(1, 1000)
