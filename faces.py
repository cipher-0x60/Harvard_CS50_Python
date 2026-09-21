def main():
    # 1. Get input from the user
    user_input = input("Type something with :) or :(: ")

    # 2. Convert the emoticons using the helper function
    converted_text = convert(user_input)

    # 3. Print the final result
    print(converted_text)

def convert(text):
    # Chain .replace() methods to swap out both emoticons
    return text.replace(":)", "🙂").replace(":(", "🙁")

# Call the main function to run the program
if __name__ == "__main__":
    main()
