user_input= input("What time is it? ")

def main():
    if convert(user_input) >=7.0 and convert(user_input) <= 8.0:
        print("Breakfast Time ")
    elif convert(user_input) >=12.0 and convert(user_input) <= 13.0:
        print("Lunch Time ")
    elif convert(user_input) >=18.0 and convert(user_input) <= 19.0:
        print("Lunch Time ")

def convert(time):
    converted_time = time.replace(':','.')
    return float(converted_time)
    

if __name__ == "__main__":
    main()