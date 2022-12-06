                                                                  # Torism Management System

                                                    

import os
import csv
from csv import DictWriter
from datetime import date

def cnic_check(cnic):#Here we are making CNIC a unique ID
    list = ["First Name", "Second Name", "Age", "Cnic number", "Mobile number","Booking Date",
            "Destination Chargers","Resort Charges", "Transportation Charges", "Food Charges", "Total Bill"]
    cnic_search = cnic
    x = False
    with open('Record-Tourists.csv') as f:
            DictReader_obj = csv.DictReader(f)
            for item in DictReader_obj:
                for key, val in item.items():#1st item is dictionary name 2nd one returning the key and values of the function
                    if key == "Cnic number":
                        if val == cnic_search:
                            print("CNIC EXITS")
                            x = True
            if x == True:
                        return x
            else:
                return x

def mobile_number_check(mobile_number):
    list = ["First Name", "Second Name", "Age", "Cnic number", "Mobile number","Booking Date", "Destination Chargers",
            "Resort Charges", "Transportation Charges", "Food Charges", "Total Bill"]
    mobile_number_search = mobile_number
    x = False
    with open('Record-Tourists.csv') as f:
            DictReader_obj = csv.DictReader(f)
            for item in DictReader_obj:
                for key, val in item.items():
                    if key == "Mobile number":
                        if val == mobile_number_search:
                            x = True
            if x == True:
                        return x
            else:
                return x

def admin():
    print("""
                                        **************************************************************
                                        *                                                            *
                                        *                      ADMIN                                 *
                                        *                                                            *
                                        **************************************************************""")
    username = input("Username: ").lower() #User name is admin(can be in lowercase and upper cases)
    password = input("Password: ") #Password is also admin(Strictly in lower case)
    tries = 2
    while (username != "admin") or (password != "admin"): #Check if username and password is wrong
        while tries > 0:
            if (username != "admin") or (password != "admin"):
                print(f"""Wrong username or password. {tries} number of tries remain. Enter user name and password again""")
                tries -= 1
                username  = input("Username: ")
                password = input("Password: ")
                if (username == "admin") and (password == "admin"):
                    print("Approved \n")
                    list = ["1.Add record", "2. View record", "3. Search record", "4. Returning back to the main menu"]
                    for i in list:
                        print(i)
                    option = input("Enter any serial number to choose the option. \n>")
                    if option == "1":
                        First_name,Second_name, age, cnic, mobile_number = add_record()
                        dest_charges, resort_charges, transportation_charges, Food_charges, total_bill = packages()
                        billing(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges,Food_charges, total_bill)
                        record_saver_tourists(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges, Food_charges, total_bill)
                    if option =="2":
                        view_record()
                    if option == "3":
                        search_record()
                    if option == "4":
                        start()
                    else:
                        while not option.isdigit() or int(option) not in range(0,4):
                            option = input("Error! Please Enter any serial number to choose the option. \n>")
                            if option == "1":
                                First_name,Second_name, age, cnic, mobile_number = add_record()
                                dest_charges, resort_charges, transportation_charges, Food_charges, total_bill = packages()
                                billing(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges,transportation_charges, Food_charges, total_bill)
                                record_saver_tourists(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges,transportation_charges, Food_charges, total_bill)
                            if option == "2":
                                view_record()
                            if option == "3":
                                search_record()
                            if option == "4":
                                start()

        print("\nReached maximum number of tries. Program Ended.")
        start()


    if (username == "admin") and (password == "admin"):
        list = ["1. View record", "2. Add record","3. Search record", "4. Returning back to main menu"]
        for i in list:
            print(i)
        option = input("Please Enter any serial number to choose the option. \n>")
        if option == "1":
            view_record()
        if option == "2":
            First_name,Second_name, age, cnic, mobile_number = add_record()
            dest_charges, resort_charges, transportation_charges, Food_charges, total_bill = packages()
            billing(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges, Food_charges,total_bill)
            record_saver_tourists(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges,Food_charges, total_bill)
        if option == "3":
            search_record()
        if option == "4":
            start()
        else:
            while not option.isdigit() or int(option) not in range(0, 5):
                option = input("Error! Please Enter any serial number to choose the option. \n>")
                if option == "1":
                    view_record()
                if option == "2":
                    First_name,Second_name, age, cnic, mobile_number = add_record()
                    dest_charges, resort_charges, transportation_charges, Food_charges, total_bill = packages()
                    billing(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges,Food_charges, total_bill)
                    record_saver_tourists(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges,transportation_charges, Food_charges, total_bill)
                if option == "3":
                    search_record()
                if option == "4":
                    start()

def tourist_control():
    list = ["1. Already Registered", "2. Apply for Registration "]
    for i in list:
        print(i)
    option = input("Enter any of the above serial number. \n>")
    while not option.isdigit() or int(option) not in range(1, 3):
        option = input("Error! Please Enter any of the above serial number. \n>")

    if option == "1":
        mobile_number = input("Enter your mobile numer: ")
        while not mobile_number.isdigit() or len(mobile_number) != 11:
            mobile_number = input("Enter your mobile numer again: ")
        if mobile_number.isdigit() and len(mobile_number) == 11:
            p = mobile_number_ceck(mobile_number)
            if p == True:
                print("Given access")
            if p == False:
                print("Mobile number didn't Exists Returning back to main menu")
                start()

        cnic = input("Enter your cnic: ")
        while not cnic.isdigit() or len(cnic) != 13:
            cnic = input("Enter your cnic again: ")
        if cnic.isdigit() or len(cnic) == 13:
            a = cnic_check(cnic)
            if a == True:
                print("Given access")
            if a == False:
                print("CNIC didn't Exists Returning back to main menu")
                start()

        choices = ["1. View Record", "2. Search record", "3. Return back to the main Menu"]
        for i in choices:
            print(i)
        select = input("Enter any of the above serial number. \n>")
        while not select.isdigit() or int(select) not in range(1, 4):
            select = input("Error! Please Enter any of the above serial number. \n>")

        if select == "1":
            view_record()
        if select == "2":
            search_record()
        if select == "3":
            print("Returning back to Main menu")
            start()
    if option == "2":
        First_name,Second_name, age, cnic, mobile_number = tourists()
        dest_charges, resort_charges, transportation_charges, Food_charges, total_bill = packages()
        billing(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges, Food_charges,
                total_bill)
        record_saver_tourists(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges,
                              Food_charges, total_bill)

def tourists():
    print("""
                                        **************************************************************
                                        *                                                            *
                                        *                    NEW TOURISTS                            *
                                        *                                                            *
                                        **************************************************************""")

    First_name = input("Enter your First name. \n>")
    while not First_name.isalpha():  # Check if digit is included in name
        print("Invalid First Name")
        First_name = input("Please! Enter your First name again. \n>")
        if not First_name.isalpha():
            print("Wrong Name. You are not allowed. Returning back to start menu\n")
            start()
    Second_name = input("Enter your Second name. \n>")
    while not Second_name.isalpha():  # Check if digit is included in name
        print("Invalid First Name")
        Second_name = input("Please! Enter your Second name again. \n>")
        if not Second_name.isalpha():
            print("Wrong Name. You are not allowed. Returning back to start menu\n")
            start()

    cnic = input("Enter your 13 digit CNIC number. \n>")
    if len(cnic) == 13:
        p = cnic_check(cnic)
        if p == True:
            print("CNIC EXISTS. PLEASE ENTER A NEW CNIC")
            start()
    while not cnic.isdigit():  # Check if alphabet is not included in name
        cnic = input("Invalid CNIC number! Please Enter CNIC number again \n>")
        if not cnic.isdigit():
            print("Wrong Cnic. You are not allowed. Returning back to start menu\n")
            start()
        else:
            p = cnic_check(cnic)
            if p == True:
                print("CNIC EXISTS. PLEASE ENTER A NEW CNIC")
                start()

    while len(cnic) != 13:  # Check if the CNIC have digits greater than or less than 13
        cnic = input("Invalid CNIC number! Please Enter CNIC number again \n>")
        if len(cnic) != 13:
            print("Wrong CNIC. You are not allowed. Returning back to start menu\n")
            start()
        else:
            p = cnic_check(cnic)
            if p == True:
                print("CNIC EXISTS. PLEASE ENTER A NEW CNIC")
                start()

    age = input("Enter your age in digits. \n>")  # Check if the age don't contain alphabets
    while not age.isdigit():
        age = input("Error! Enter your age in digits. \n>")
        if not age.isdigit():
            print("Wrong age. You are not allowed. Returning back to start menu\n")
            start()
    while int(age) < 18 or int(age) > 60:  # Check if the age is not less than 18 year and greater than 60 year
        age = input("Error! Enter your age and you must be 18 to 60 year old. \n>")
        if int(age) < 18 or int(age) > 60:
            print("Wrong age. You are not allowed. Returning back to start menu\n")
            start()

    mobile_number = input("Enter your mobile number. \n>")
    while not mobile_number.isdigit():
        mobile_number = input("Invalid mobile number! Please Enter mobile number again \n>")
        if not mobile_number.isdigit():
            print("Wrong mobile number. You are not allowed. Returning back to start menu\n")
            start()
    while len(mobile_number) != 11:  # Check if the number have less than or greater than 11 digits
        mobile_number = input("Invalid mobile number! Please Enter mobile number again \n>")
        if len(mobile_number) != 11:
            print("Wrong mobile number. You are not allowed. Returning back to start menu\n")
            start()

    return First_name, Second_name, age, cnic, mobile_number

def packages():
    print("""
                                        **************************************************************
                                        *                                                            *
                                        *                      PACKAGES                              *
                                        *                                                            *
                                        **************************************************************""")
    print("Our destinations points are: ")
    Destinations = ["1. Murree", "2. Gilgit ", "3. Swat ", "4. Kashmir ", "5. Returning back to Main menu"]
    for i in Destinations:
        print(i)  # Here printing the destinations

    dest = input("Enter Serial Number of any of Destination point mentioned above: \n> ")
    while dest == "5":
        start()

    while not dest.isdigit() or int(dest) not in range(1,6):#Here checking wether the user selecting the right serial number for destination or not
        if not dest.isdigit() or int(dest) not in range(1, 6):
            print("""We didn't get you. Sorry try again
1. Murree
2. Gilgit 
3. Swat 
4. Kashmir
5. Exit""")
            dest = input("Invalid serial number!Enter Serial Number from 1 to 4: ")
            while dest == "5":
                start()

    if dest == "1":
        dest_charges = 2000
    if dest == "2":
        dest_charges = 5000
    if dest == "3":
        dest_charges = 4000
    if dest == "4":
        dest_charges = 3000


    print("=" * 150)

    if int(dest) in range(1, 6):
        if dest == "1" or dest == "2" or dest == "3" or dest == "4":
            print("Our resorts are as following")
            resort = ["1. Platinum resort", "2. Gold resort", "3. Silver resort", "4. Bronze resort", "5. Returning back to Main menu"]
            for i in resort:
                print(i)
            resort = input("Select any of the above resort option. \n> ")
            if resort == "5":
                start()
            while not resort.isdigit() or int(resort) not in range(1,6):  # Here checking wether the user selecting the right serial number for resort or not
                print("""We didn't get you.Sorry
1. Platinum resort
2. Gold resort
3. Silver resort
4. Bronze resort
5. Exit""")
                resort = input("Select any of the above 5 options. ")
                if resort == "5":
                    start()
    if resort == "1":
        resort_charges = 20000
    if resort == "2":
        resort_charges = 15000
    if resort == "3":
        resort_charges = 10000
    if resort == "4":
        resort_charges = 5000
    if resort == "5":
        start()

    print("=" * 150)

    if int(dest) in range(1, 6):
        if dest == "1" or dest == "2" or dest == "3" or dest == "4":
            print("Our transportation are as following\n ")
            transportation = ["1. Platinum transportation", "2. Gold transportation", "3. Silver transportation",
                              "4. Bronze transportation", "5. Returning back to Main menu"]
            for i in transportation:
                print(i)
            transportation = input("Select any of the above transportation option. \n> ")
            if transportation == "5":
                start()
            while not transportation.isdigit() or int(transportation) not in range(1,6):# Here checking wether the user selecting the right serial number for transportation or not
                print("""We didnt get you.Sorry 
1. Platinum transportation
2. Gold transportation
3. Silver transportation
4. Bronze transportation
5. Exit""")
                transportation = input("Select any of the above transportation option. \n> ")
                if transportation == "5":
                    start()

    if transportation == "1":
        transportation_charges = 15000
    if transportation == "2":
        transportation_charges = 10000
    if transportation == "3":
        transportation_charges = 5000
    if transportation == "4":
        transportation_charges = 2000

    print("=" * 150)

    if int(dest) in range(1, 6):
        if dest == "1" or dest == "2" or dest == "3" or dest == "4":
            print("Our Food are as following\n ")
            Food = ["1. Category.A Food", "2. Category.B Food", "3. Category.C Food", "4. Category.D Food", "5. Returning back to Main menu"]
            for i in Food:
                print(i)

            Food = input("Select any of the above Food option. \n>")
            if Food == "5":
                start()
            while not Food.isdigit() or int(Food) not in range(1,6):  # Here checking wether the user selecting the right serial number for Food or not
                print("""We didn't get you.Sorry 
1. Category.A Food
2. Category.B Food
3. Category.C Food
4. Category.D Food
5. Exit""")

                Food = input("Select any of the above 5 options. \n>")
                if Food == "5":
                    start()

    if Food == "1":
        Food_charges = 15000
    if Food == "2":
        Food_charges = 10000
    if Food == "3":
        Food_charges = 5000
    if Food == "4":
        Food_charges = 2000

    print("=" * 150)

    total_bill = dest_charges + resort_charges + transportation_charges + Food_charges
    return dest_charges, resort_charges, transportation_charges, Food_charges, total_bill

def billing(First_name,Second_name, age, cnic, mobile_number, dest_charges, resort_charges, transportation_charges,
            Food_charges, total_bill):
    print("""
                                        **************************************************************
                                        *                                                            *
                                        *                         BILLING                            *
                                        *                                                            *
                                        **************************************************************""")

    print(f"""
                                                ********************************************
                                                *          CHARGES AND TOTAL BILL          *
                                                ********************************************
                                                  Name: {First_name} {Second_name}
                                                  Age: {age}      
                                                  Mobile Number: {mobile_number} 
                                                  Cnic: {cnic}

                                                  Destination Charges: {dest_charges}           
                                                  Resort Charges: {resort_charges}
                                                  Transportation Charges: {transportation_charges}
                                                  Food Charges: {Food_charges}
  
                                                  Total_bill = {total_bill}

                                                  Note: We accept cash only. Good Luck
""")

def Exit():
    print("Are you Sure You don't want to travel with us.")
    Exit = ["1. Yes", "2. No"]
    for i in Exit:
        print(i)
    option = input("Choose any of the above serial number. \n>")
    while not option.isdigit()or int(option) not in range(1,3):#Here checking wether the user selecting the right serial number for option or not
        print("""Wrong option. Please try again
1. Yes
2. No""")
        option = input("Error! Choose any of the above serial number. \n>")
    if option == "1":
        print("Take care. Good Bye")
    if option == "2":
        start()

def add_record():
    print("""
                                        **************************************************************
                                        *                                                            *
                                        *                      WELCOME ADMIN                         *
                                        *                                                            *
                                        **************************************************************""")

    First_name = input("Enter your First name. \n>")
    while not First_name.isalpha():  # Check if digit is included in name
        print("Invalid First Name")
        First_name = input("Please! Enter your First name again. \n>")
        if not First_name.isalpha():
            print("Wrong Name. You are not allowed. Returning back to start menu\n")
            start()
    Second_name = input("Enter your Second name. \n>")
    while not Second_name.isalpha():  # Check if digit is included in name
        print("Invalid First Name")
        Second_name = input("Please! Enter your Second name again. \n>")
        if not Second_name.isalpha():
            print("Wrong Name. You are not allowed. Returning back to start menu\n")
            start()

    cnic = input("Enter 13 digit CNIC number. \n>")
    if len(cnic) == 13:
        p = cnic_check(cnic)
        if p == True:
            print("CNIC EXISTS. PLEASE ENTER A NEW CNIC")
            start()
    while not cnic.isdigit():  # Check if alphabet is not included in name
        cnic = input("Invalid CNIC number! Please Enter CNIC number again \n>")
        if not cnic.isdigit():
            print("Wrong Cnic. You are not allowed. Returning back to start menu\n")
            start()
        else:
            p = cnic_check(cnic)
            if p == True:
                print("CNIC EXISTS. PLEASE ENTER A NEW CNIC")
                start()

    while len(cnic) != 13:  # Check if the CNIC have digits greater than or less than 13
        cnic = input("Invalid CNIC number! Please Enter CNIC number again \n>")
        if len(cnic) != 13:
            print("Wrong CNIC. You are not allowed. Returning back to start menu\n")
            start()
        else:
            p = cnic_check(cnic)
            if p == True:
                print("CNIC EXISTS. PLEASE ENTER A NEW CNIC")
                start()

    age = input("Enter age in digits. \n>")  # Check if the age don't contain alphabets
    while not age.isdigit():
        age = input("Error! Enter your age in digits. \n>")
        if not age.isdigit():
            print("Wrong age. You are not allowed. Returning back to start menu\n")
            start()
    while int(age) < 18 or int(age) > 60:  # Check if the age is not less than 18 year and greater than 60 year
        age = input("Error! Enter your age and you must be 18 to 60 year old. \n>")
        if int(age) < 18 or int(age) > 60:
            print("Wrong age. You are not allowed. Returning back to start menu\n")
            start()

    mobile_number = input("Enter your mobile number. \n>")
    while not mobile_number.isdigit():
        mobile_number = input("Invalid mobile number! Please Enter mobile number again \n>")
        if not mobile_number.isdigit():
            print("Wrong mobile number. You are not allowed. Returning back to start menu\n")
            start()
    while len(mobile_number) != 11:  # Check if the number have less than or greater than 11 digits
        mobile_number = input("Invalid mobile number! Please Enter mobile number again \n>")
        if len(mobile_number) != 11:
            print("Wrong mobile number. You are not allowed. Returning back to start menu\n")
            start()

    return First_name,Second_name, age, cnic, mobile_number

def record_saver_tourists(First_name,Second_name, age, cnic, mobile, dest_charges, resort_charges, transportation_charges,Food_charges, total_bill):
    path = os.getcwd()#Current working diectory # it find the the location of the python file
    if os.path.exists(path + "/" + "Record-Tourists.csv"):#Here we are chechking if the CSV file exist it just gonna append values in the desire keys

        f_names = ["First Name", "Second Name", "Age", "Cnic number", "Mobile number",
                   "Booking Date", "Destination Chargers",
                   "Resort Charges", "Transportation Charges", "Food Charges",
                   "Total Bill"]

        today = date.today()
        dated = today.strftime("%B %d, %Y")#string fomart time # setting the format of the date we are getting in varaible today
        record_tourist = {'First Name': First_name, 'Second Name': Second_name, 'Age': age, 'Cnic number': cnic, 'Mobile number': mobile,
                          'Booking Date': dated,
                          'Destination Chargers': dest_charges, 'Resort Charges': resort_charges,
                          'Transportation Charges': transportation_charges,
                          'Food Charges': Food_charges, 'Total Bill': total_bill}

        with open("Record-Tourists.csv", 'a+') as write_obj:
            dict_writer = DictWriter(write_obj, fieldnames=f_names)
            dict_writer.writerow(record_tourist)

    else:

        f_names = ["First Name", "Second Name", "Age", "Cnic number", "Mobile number",
                   "Booking Date", "Destination Chargers",
                   "Resort Charges", "Transportation Charges", "Food Charges",
                   "Total Bill"]
        today = date.today()
        dated = today.strftime("%B %d, %Y")#string fomart time
        record_tourist = [{'First Name': First_name, 'Second Name': Second_name, 'Age': age, 'Cnic number': cnic, 'Mobile number': mobile, 'Booking Date': dated,
                           'Destination Chargers': dest_charges, 'Resort Charges': resort_charges,
                           'Transportation Charges': transportation_charges, 'Food Charges': Food_charges,
                           'Total Bill': total_bill}]
        with open('./Record-Tourists.csv', 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=f_names)
            writer.writeheader()#Making columns of the of csv file
            writer.writerows(record_tourist)
    start()

def view_record():
    list = ["First Name", "Second Name", "Age", "Cnic number", "Mobile number",
            "Booking Date", "Destination Chargers", "Resort Charges",
            "Transportation Charges", "Food Charges", "Total Bill"]
    with open('Record-Tourists.csv') as f:
        DictReader_obj = csv.DictReader(f)

        for item in DictReader_obj:
            for i in list:
                print(i, ":", item[i], end=", ")
            print("\n")
    start()

def search_record():
    list = ["First Name", "Second Name", "Age", "Cnic number", "Mobile number", "Booking Date", "Destination Chargers", "Resort Charges",
            "Transportation Charges", "Food Charges", "Total Bill"]
    x = input(""" Please enter serial number of search method
                  1. CNIC
                  2. First Name 
                  3. Mobile number \n> """)
    while not x.isdigit() or int(x) not in range(1, 4):
        x = input(""" Error! Please enter serial number of search method
                          1. CNIC
                          2. First Name 
                          3. Mobile number \n> """)
    if x == "1":
        cinc_search = input("Enter CNIC: ")
        while not cinc_search.isdigit() or not len(cinc_search) == 13:
            cinc_search = input("Enter CNIC again: ")

        x = False
        with open('Record-Tourists.csv') as f:
            DictReader_obj = csv.DictReader(f)
            for item in DictReader_obj:
                list1 = []
                list2 = []
                for key, val in item.items():

                    list1.append(key)
                    list2.append(val)

                    if key == "Cnic number":
                        x = False
                        if val == cinc_search:
                            x = True
                if x == True:
                    for i in range(0, len(list1)):
                        print(list1[i], ":", list2[i], end=', ')
            if x != True:
                print("No Record found")


    if x == "2":
        name_search = input("Enter name: ")
        while not name_search.isalpha():
            name_search = input("Enter name again: ")
        x = False
        with open('Record-Tourists.csv') as f:
            DictReader_obj = csv.DictReader(f)
            for item in DictReader_obj:
                list1 = []
                list2 = []
                for key, val in item.items():

                    list1.append(key)
                    list2.append(val)

                    if key == "First Name":
                        x = False
                        if val == name_search:
                            x = True
                if x == True:
                    for i in range(0, len(list1)):
                        print(list1[i], ":", list2[i], end=', ')
            if x != True:
                print("No Record found")
    if x == "3":
        mobile_number = input("Enter Mobile Number: ")
        while not mobile_number.isdigit() or not len(mobile_number) == 11:
            mobile_number = input("Enter Mobile Number again: ")
        x = False
        with open('Record-Tourists.csv') as f:
            DictReader_obj = csv.DictReader(f)
            for item in DictReader_obj:
                list1 = []
                list2 = []
                for key, val in item.items():

                    list1.append(key)
                    list2.append(val)

                    if key == "Mobile number":
                        x = False
                        if val == mobile_number:
                            x = True
                if x == True:
                    for i in range(0, len(list1)):
                        print(list1[i], ":", list2[i], end=', ')
            if x != True:
                print("No Record found")

    start()

def end():
    print("""
                                        **************************************************************
                                        *                                                            *
                                        *         Sorry Program Ended Due to Invalid inputs          *
                                        *                                                            *
                                        **************************************************************""")

def start():
    print("""
******************************************************************************************************************************************************
*                                                                                                                                                    *
*                                                    TOURISM MANAGEMENT SYSTEM                                                                       *
*                                                            BY ATA-UL-HAQ                                                                           *
*                                                               AYESHA HISSAM                                                                        *
*                                                               SHAZMIN NASIR                                                                        *
*                                                                                                                                                    *
******************************************************************************************************************************************************
     """)

    print("Welcome To Nature Tourists \n ")
    print("Choose if you want to login as")
    choose= ["1. Admin", "2. Tourists", "3. Refreshing the screen"]
    for i in choose:
        print(i)
    choose= input("Choose any of the above options. \n>")
    while not choose.isdigit() or int(choose) not in range(1,4):
        print("Invalid serial number")
        choose = input("Enter Serial Number of the option mentioned above: ")

    if choose == "1":
        admin()

    if choose == "2":
        tourist_control()

    if choose== "3":
        start()

start()

