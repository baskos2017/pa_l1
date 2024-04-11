def even_decorator(func):
    def wrapper():
        for num in func():
            if num % 2 == 0:
                yield num
    return wrapper

@even_decorator
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fib_generator()

for _ in range(10):
    print(next(fibonacci))