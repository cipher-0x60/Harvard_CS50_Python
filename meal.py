

def main():

    user_input= input("What time is it? ")
    time_2 = convert(user_input)

    if  time_2 >=7.0 and  time_2 <= 8.0:
        print("Breakfast Time ")
    elif  time_2 >=12.0 and  time_2 <= 13.0:
        print("Lunch Time ")
    elif  time_2 >=18.0 and time_2 <= 19.0:
        print("Dinner Time ")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60.0
    

if __name__ == "__main__":
    main()