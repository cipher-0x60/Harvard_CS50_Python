def addition(x, z):
    return float(x + z)

def subtraction(x, z):
    return float(x - z)

def mode_remainder(x, z):
    return float(x % z)

def multiplication(x, z):
    return float(x * z)

def division(x, z):
    return float(x / z)

def floor_division(x, z):
    return float(x // z)

def exponential(x, z):
    return float(x ** z)


def interpreter_math():

    expression = input("Expression: ")

    x_str, y, z_str = expression.split(" ")
    x = int(x_str)
    z = int(z_str)


    if y == "+":
        result = addition(x, z)
    elif y == "-":
        result = subtraction(x, z)
    elif y == "%":
        result = mode_remainder(x, z)
    elif y == "*":
        result = multiplication(x, z)
    elif y == "/":
        result = division(x, z)
    elif y == "//":
        result = floor_division(x, z)
    elif y == "**":
        result = exponential(x, z)
    else:
        print("Provide the right math operator sign.")
        return


    print(f"{result:.1f}")


interpreter_math()
