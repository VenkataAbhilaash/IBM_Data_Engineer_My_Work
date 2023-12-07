print("Code for finding the Leap Year.")

Number = int(input("Enter the year you want to find out ?"))

if Number%4==0:
    if Number%100==0:
        if Number%400==0:
            print("A Leap Year.")
        else:
            print("Not a Leap Year.")
    else:
        print("A Leap Year.")
else:
    print("Not A Leap Year.")