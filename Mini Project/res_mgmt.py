from restaurant import Res
import os

class ResMgmt:
    
    def addMenu(m):
        fp = open("menu.txt","a")
        fp.write(str(m))
        fp.write("\n")
        fp.close()


    def readMenu():
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            data = fp.read()
            print(data)
            fp.close()


    def searchMenuid(id):
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            try:
                for line in fp:
                    line = line.strip()
                    line = line.split(",")
                    if(id == int(line[0])):
                        print(line)
                        break

            except:
                print("Record not found")
            else:
                print("Please Enter Valid ID")
            fp.close()


    def searchMenuname(name):
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            try:
                for line in fp:
                    line = line.strip()
                    line = line.split(",")
                    if(name == str(line[1])):
                        print(line)
                        break
            except:
                print("Record not found")
            else:
                print("Please Enter Valid Name")
                    
            fp.close()


    def searchMenutype(type):
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            try:
          
                for line in fp:
                    line = line.strip()
                    line = line.split(",")
                    if(type == str(line[3])):
                        print(line)
                        
            except:
                print("Record not found")
            else:
                print("Please Enter Valid Type")
            
            fp.close()


    def deleteMenu(id,name):
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            found = False
            menu = []
            for line in fp:
                line = line.strip()
                line = line.split(",")
                if(id == int(line[0]) and name == line[1]):
                    found = True
                else:
                    menu.append(line)
                    
            fp.close()

            if(found):
                fp = open("menu.txt","w")
                for x in menu:
                    x = ",".join(x)
                    x += "\n"
                    fp.write(x)
                fp.close()
                print("Record deleted successfully..")

            else:
                print("Record not found")

            #print(menu)


    def editMenu(id,name):
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            found = False
            menu = []
            for line in fp:
                line = line.strip()
                line = line.split(",")
                if(id == int(line[0]) and name == line[1]):
                    found = True
                    ans = input("Do you wish to change name (y/n) : ")
                    if(ans.lower() == "y"):
                        line[1] = input("Enter new name : ")
                    ans = input("Do you wish to change price (y/n) : ")
                    if(ans.lower() == "y"):
                        line[2] = input("Enter new price : ")
                    ans = input("Do you wish to change type (y/n) : ")
                    if(ans.lower() == "y"):
                        line[3] = input("Enter new type : ")
                    ans = input("Do you wish to change quantity (y/n) : ")
                    if(ans.lower() == "y"):
                        line[4] = input("Enter new quantity : ")
                
                menu.append(line)
            #print(menu)
            fp.close()

            if(found):
                fp = open("menu.txt","w")
                for x in menu:
                    x = ",".join(x)
                    x += "\n"
                    fp.write(x)
                fp.close()
                print("Record edited successfully..")
                
            else:
                print("Record not found")
            

    def addCart(h):
        fp = open("wishlist.txt","a")
        fp.write(str(h))
        fp.write("\n")
        fp.close()


    def orderMenu(id):
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            found = False
            menu = []
            for line in fp:
                line = line.strip()
                line = line.split(",")
                if(id == int(line[0])):
                    found = True

                    name = line[1]
                    type = line[3]
                    qty = int(input("Enter Quantity : "))   
                    price = qty * int(line[2])
                    h1 = Res(id,name,price,type,qty)
                    ResMgmt.addCart(h1)
                    line[4] = str(int(line[4]) - qty)
                    
                menu.append(line)
            fp.close()

            if(found):
                fp = open("menu.txt","w")
                for x in menu:
                    x = ",".join(x)
                    x += "\n"
                    fp.write(x)
                fp.close()
                print("Added to Wishlist..")
                
            else:
                print("Record not found")


    def bill():
        try:
            fp = open("wishlist.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            amount = 0
            print("---------------------------------------------------")
            print("--------ID-------Name----------Qty-----Price-------")
            print("---------------------------------------------------\n")
            for line in fp:
                line = line.strip()
                line = line.split(",")
                amount += int(line[2])
                print("%10s %10s %10s %10s"%(line[0],line[1],line[4],line[2]))
                print("\n")
            print("---------------------------------------------------")
            print("---------------------------------------------------")
            print("TOTAL : ",amount,"Rs/- only")
            print("---------------------------------------------------")
        
            fp.close()


    def confirmord():
        try:
            fp = open("wishlist.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            
            for line in fp:
                line = line.strip()
            
                print('''Thank you for being our valued customer. 
We are greatful for the pleasure of serving you..
We hope your experience was awesome and can't wait to see you again..
            ''')
                break

            fp.close()
            os.remove('wishlist.txt')


    def cancelord() :
        try:
            fp = open("menu.txt","r")
        except FileNotFoundError:
            print("File does not exists..")
        else:
            menu = []
            found = False
            for line in fp:
                line = line.strip()
                line = line.split(",")
                try:
                    p = open("wishlist.txt","r")
                except FileNotFoundError:
                    print("File does not exits..")
                else:
                    menu1 = []
                    for line1 in p:
                        line1 = line1.strip()
                        line1 = line1.split(",")
                        if(line[0] == line1[0]):
                            found = True
                            line[4] = str(int(line[4]) + int(line1[4]))
                        else:
                            menu1.append(line1)

                    if(found):
                        fp = open("wishlist.txt","w")
                        for line2 in menu1:
                            line2 = ",".join(line2)
                            line2 += "\n"
                            fp.write(line2)
                        fp.close()
                        
                menu.append(line)
            fp.close()

            if(found):
                fp = open("menu.txt","w")
                for line2 in menu:
                    line2 = ",".join(line2)
                    line2 += "\n"
                    fp.write(line2)
                fp.close()
                print("Your Oder is Cancled.. Thank You for Visiting..")

            else:
                print("Record not Find..")     
        