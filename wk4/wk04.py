def add(x, y):
    return x + y
subtract = lambda x, y: x - y
square = lambda x: x*x
is_even = lambda x: x % 2 == 0
numbers = [1, 2, 3, 4, 5]
square_numbers = list(map(square, numbers))
even_numbers = list(filter(is_even, numbers))

print(add(3, 5))
print(subtract(10, 4))
print(square(4))