from admin import *
from user import *

ch = 0

while(ch != 3):

    print("\n\t-----* WELCOME TO RESTAURANT MANAGEMENT SYSTEM *-----\n")
    print('''                        |-------------------|
                        |                   |
                        |      1.Admin      |
                        |      2.User       |
                        |      3.Exit       |
                        |                   |
                        |-------------------|
        ''')

    try:
        ch = int(input("Enter Your Choice : \n"))

    except:
        print("Please Enter Valid Choice")  
        
    else:

        if(ch == 1):
            admin()

        elif(ch == 2):
            user()

        elif(ch == 3):
            print("Thank you for visit our restaurant...")
            break
    
        else:
            print("Invalid Choice..!")
        