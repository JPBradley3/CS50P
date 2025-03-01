def interpreter():
    expression = input("Expression: ").strip(" ")

    value = expression.split(' ')

    x = int(value[0])
    y = value[1]
    z = int(value[2])

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    else:
        result = x / z

    print(f'{result:.1f}')

interpreter()
