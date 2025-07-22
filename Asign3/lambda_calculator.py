add = lambda a, b: a + b
subt = lambda a, b: a - b
multp = lambda a, b: a * b
divide = lambda a, b: "Error: Cannot divide by zero" if b == 0 else a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print("Addition:", add(x, y))
    print("Subtraction:", subt(x, y))
    print("Multiplication:", multp(x, y))
    print("Division:", divide(x, y))
