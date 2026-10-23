camelCase = input("camelCase: ")
snake_case = []
for charector in camelCase:
    if charector.isupper():
        snake_case.append("_")
    snake_case.append(charector.lower())

snake_case = "".join(snake_case)
print(f"snake_case: {snake_case}")
