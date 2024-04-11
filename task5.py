my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_square = []
for i in filter(lambda x: x % 2 != 0, my_list):
    odd_square.append(i ** 2)

print(odd_square)
