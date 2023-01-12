from restaurant import Res
from res_mgmt import ResMgmt
import random

def user():
    

    createid = input("Create userid : ")
    pwd = input("Create Password : ")
    userid = input("Enter userid : ")
    password = input("Enter password : ")

    if(userid == createid and password == pwd):
        print("Your ID and Password is Correct")
        x = random.randint(1000,9999)
        print("Captcha : ",x)
        captcha = int(input("Enter Captcha : "))

        if(x == captcha):
            print("\n\t\t---------*  Welcome to Khandesh Darbar Restaurant  *---------\n")

            choice , ch1 = 0 , 0
            while(choice != 7):

                print("\n\t\t-------------------------------------------------------------\n")
                print('''
                        \t\t1. Show Menu
                        \t\t2. Search Menu
                        \t\t3. Select Menu
                        \t\t4. Show Bill
                        \t\t5. Confirm Order
                        \t\t6. Cancel Order
                        \t\t7. Exit
                    ''')
                print("\t\t-------------------------------------------------------------\n")

                try:
                    choice = int(input("Enter Your Choice : \n"))
                except:
                    print("Please Enter Valid Choice")
                else:

                    if(choice == 1):
                        ResMgmt.readMenu()

                    elif(choice == 2):
                        while(ch1 != 4):
                            print("\n\t\t-------------------------------------------------------------\n")
                            print("\t\t1.Search ID")
                            print("\t\t2.Search Name")
                            print("\t\t3.Search Type")
                            print("\t\t4.Go Back")
                            print("\t\t-------------------------------------------------------------\n")

                            try:
                                ch1 = int(input("Enter Your Choice : \n"))
                            except:
                                print("Please Enter Valid Choice")
                            else:

                                if(ch1 == 1):
                                    try:
                                        id = int(input("Enter Id : "))
                                    except:                                            
                                        print("Please Enter Valid Id")
                                    else:
                                        ResMgmt.searchMenuid(id)

                                elif(ch1 == 2):
                                    try:
                                        name = input("Enter Name : ")
                                    except:
                                        print("Please Enter Valid Name")
                                    else:
                                        ResMgmt.searchMenuname(name)

                                elif(ch1 == 3):
                                    try:
                                            type = input("Enter Type : ")
                                    except:
                                        print("Please Enter Valid Type")
                                    else:
                                            ResMgmt.searchMenutype(type)

                                elif(ch1 == 4):
                                    print("Go Back")
                                    break

                                else:
                                   print("Please Enter Correct Option..!!")

                    elif(choice == 3):
                        try:
                            id = int(input("Enter id : "))
                        except:
                                print("Please Enter Valid Id")
                        else:
                            ResMgmt.orderMenu(id)

                    elif(choice == 4):
                        ResMgmt.bill()

                    elif(choice == 5):
                        ResMgmt.confirmord()

                    elif(choice == 6):
                        ResMgmt.cancelord()
                        
                    
                    elif(choice == 7):
                        print("Exit")
                        break

                    else:
                        print("Invalid Choice..!!")

        else:
            print("Sorry... You are failed...")
            
    else:
        print("Please Enter Correct ID and Password ...")    

