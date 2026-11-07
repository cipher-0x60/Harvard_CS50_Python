vowels = ["A","a","E","e","I","i","O","o","U","u"]
usr_input = (input("Input: "))

for i in usr_input:
    if i not in vowels:
        print(i, end="")
