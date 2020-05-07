import random
from os import remove
from textwrap import dedent
from datetime import datetime

time_stamp = datetime.now(tz=None)


def sessionUse(Username, sessions):
    accounts = {
        "1": "Current Account",
        "2": "Savings account",
        "3": "Fixed Deposit Account"
    }

    acti__vity = input("1. Create a new bank account\n2. Check Account details\n3. Logout\nType in option: ")
    if acti__vity == "1":
        account_name = input("Enter your Account Name: ")
        while True:
            try:
                opening_balance = int(input("Enter Opening balance (In figures): "))
                break
            except:
                print("Enter an amount in figures")
        print(dedent("""
                1. Current Account
                2. Savings account
                3. Fixed Deposit Account"""))
        while True:
            account_type = input("Type in Option (1, 2, or 3): ")
            if "1" or "2" or "3" in account_type:
                account_type = accounts.get(account_type)
                break
            else:
                print("Choose the correct option")
        account_emailaddress = input("Enter Account Email: ")
        randomlist = random.sample(range(0, 9), 9)#generating account numbers
        num_list = [str(x) for x in randomlist]
        account_number = ''.join(num_list)
        print(f"Account number: {account_number}")

        customer_details = {"account_name":account_name, "opening_balance":opening_balance, "account_type":account_type, "account_emailaddress":account_emailaddress, "account_number":account_number}
        customer_file = open("customer.txt", 'a+')
        customer_file.write(f"{str(customer_details)}\n")
        customer_file.close()
        sessions.write(f"{time_stamp}: @{Username} Created a new {account_type} account\n")

        sessionUse(Username, sessions)

    elif acti__vity == "2":
        customer_details = open("customer.txt", "r").read()
        print(customer_details)
        sessionUse(Username, sessions)

    elif acti__vity == "3":
        sessions.write(f"{time_stamp}: @{Username} logged out\n")
        sessions.close()
        remove("session")
        first_page()


def login():
    while True:
        Username = input("Enter your Username: ")
        password = input("Enter your password: ")
        staff_log = open("staff.txt","r+").read()
        staff_list = staff_log.splitlines()

        newStaffList = []
        for staff in staff_list:
            newStaffList.append(staff.split())

        logged = False
        count = 0
        for staff in newStaffList:
            count += 1
            if Username == staff[0] and password == staff[1]:
                logged = True
                sessions = open("session", "w+")
                sessions.write(f"{time_stamp}: @{Username} logged in\n")
                sessions = open("session", "a+")
                sessionUse(Username, sessions)
            if logged is False and count == len(newStaffList):
                print("You are not a staff\n")


def first_page():
    first_page_choice = input("1. Login\n2. Close App\nType in option: ")
    while True:
        if first_page_choice == "1":
            login()
        elif first_page_choice == "2":
            exit(0)
        else:
            print("Enter a valid option!")


print("Welcome to the Bank of spain")
first_page()
