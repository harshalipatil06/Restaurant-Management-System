from restaurant import Res
from res_mgmt import ResMgmt
import random

def admin():

    userid = 'Harshali@0608'
    password = '54321'
    userid = input("Enter userid: ")
    password = input("Enter password: ")

    if(userid == 'Harshali@0608' and password == '54321'):
        print("Your ID and Password is Correct")
        x = random.randint(1000,9999)
        print("Captcha: ",x)
        captcha = int(input("Enter Captcha: "))

        if(x == captcha):
            print("\n\t\t---------*  Welcome to Khandesh Darbar Restaurant  *---------\n")
           
            choice , ch1 = 0 , 0
            while(choice != 6):

                print("\t\t-------------------------------------------------------------\n")
                print('''
                         \t\t1.Add new Menu
                         \t\t2.Show all Menu
                         \t\t3.Search Menu
                         \t\t4.Delete Menu
                         \t\t5.Edit Menu
                         \t\t6.Exit
                    ''')
                print("\t\t-------------------------------------------------------------\n")

                try:
                    choice = int(input("Enter your choice: \n"))
                except:
                    print("Please Enter Valid ID/Name")
                else:
                    if(choice == 1):
                        try:
                            id = int(input("Enter id : "))                        
                            name = input("Enter name : ")
                            price = int(input("Enter price : "))
                            type = input("Enter type : ")
                            qty = int(input("Enter quantity : "))
                            m1 = Res(id,name,price,type,qty) 
                        except:
                            print("Please Enter Valid Details")
                        else:
                            ResMgmt.addMenu(m1)

                    elif(choice == 2):
                        ResMgmt.readMenu()

                    elif(choice == 3):
                        while(ch1 != 4):
                            print("\t\t-------------------------------------------------------------\n")
                            print("\t\t1.Search ID")
                            print("\t\t2.Search Name")
                            print("\t\t3.Search Type")
                            print("\t\t4.Go Back")
                            print("\n\t\t-------------------------------------------------------------\n")

                            try:
                                ch1 = int(input("Enter Your Choice : \n"))
                            except:
                                print("Please Enter Valid Choice")
                            else:
                                if(ch1 == 1):
                                    try:
                                        id = int(input("Enter Id : "))
                                    except:
                                        print("Please Enter Valid ID")
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

                    elif(choice == 4):
                        try:
                            id = int(input("Enter id : "))
                            name = input("Enter name : ")
                        except:
                            print("Please Enter Valid ID/Name")
                        else:
                            ResMgmt.deleteMenu(id,name)

                    elif(choice == 5):
                        try:
                            id = int(input("Enter id : "))
                            name = input("Enter name : ")
                        except:
                            print("Please Enter Valid ID/Name")
                        else:
                            ResMgmt.editMenu(id,name)

                    elif(choice == 6):
                        print("Exit")
                        break

                    else:
                        print("Invalid choice..!!")

        else:
            print("Sorry... You are failed...")
    else:
        print("Please Enter Correct ID and Password ...")

