def multiply(x, y):
    return x * y


def curried_multiply(x):
    def second_arg(y):
        return x * y
    return second_arg


one_arg = curried_multiply(2)

two_arg = curried_multiply(3)(2)

print(multiply(2, 3))
print(one_arg(3))
print(two_arg)
