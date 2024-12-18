print("SELECT YOUR RIDE: ")
print("!. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if(choice == 1 ):
    print("What Type Of A Bike")
    print("1. With gear")
    print("2. gearless")

    choice2=int(input("Enter your choice2: "))
    if choice2==1:
         print("you have selected a bike with gear")
    else:
         print("You have selected a gearless bike")

elif(choice == 2):
     print("What Type Of A Car")
     print("1. Sedan")
     print("2.XUV")

     choice3=int(input("enter your choice: "))
     if choice3==1:
          print("You have selected sedan")
     else:
          print("You have selected XUV")

else:
     print("Invalid")     