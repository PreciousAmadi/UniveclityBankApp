import random
import time

def random_otp(n):
    otp = '0'
    for i in range(n):
        otp = otp+ str(random.choice(range(n)))
    return otp

# Write a program that allows customers to:
# 1. Create an account with the account number generated if they do not have an account. All generated account numbers should begin with 0
# 2. Log in to the program if they have an account
# 3. Deposit money
# 4. Withdraw money from the account if they have a sufficient amount.
# 5. Users should be able to transfer money to other users in the account
# 6. Users should be able to check their account balances.
# The program should keep running until the user decides to make it log out and/or quit.
# The account data should be stored in a dictionary that looks like this:

# data = {'0123445677' : {
#         "first_name":"John",
#         "last_name" : "Doe ",
#         "login_pin" : "8424"
#         "transaction_pin": "0934",
#         "balance" : 0
#     }
# }

# d = {"key":"value", "key2":"value2"}

data = {}
data2 = {}

print("*"*31)
print("Welcome to Univelcity Bank.")
print("*"*31)


while True:
    print("What would you like to do?\n1. Login\n2. Create Account\n3. Quit")
    user_input = input("::>")

    if user_input == "2":
        print("Please enter your first name.")
        first_name = input("::>")
        print("Please enter your last name.")
        last_name = input("::>")
        print("Please create your 4-digit pin.")
        login_pin = input("::>")
        print("Please create your 4-digit transaction pin.")
        transaction_pin = input("::>")
        acct_no = random_otp(9)
        
        data2 = {"first_name": first_name,
                 "last_name": last_name,
                 "login_pin": login_pin,
                 "transaction_pin": transaction_pin,
                 "balance": 0}
        data[acct_no] = data2

        print("Creating account...")
        time.sleep(2)
        print("Completing setup...")
        time.sleep(1)
        print(f"\nWelcome {first_name}!\nYour account has been created and activated. \nYour Account number is {acct_no}\nCheers\nUnivelcity Bank.\n")

    elif user_input == "1":
        print("\nPlease enter your Account number.")
        acct_no = input("::>")
        print("\nPlease enter your 4-digit login pin.")
        pin = (input("::>"))
        data2[login_pin] = pin
        
        user_acct_no = data.get(acct_no, False)
        user_login_pin = data2.get(pin, False)

        if user_acct_no and user_login_pin:
            print(f'Welcome {first_name}.')
            print("*************************************")
            print("Press 1 to Deposit ")
            print("Press 2 to Withdraw ")
            print("Press 3 to Transfer ")
            print("Press 4 to Check Balance ")
            print("Press 5 to Exit/Quit ")
            print("*************************************")
            choice = input('::>')
            if choice == "1":
                print('Enter deposit amount')
                amount = input('::>')
                data2["balance"] = amount
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                break
            else: print('Invalid input')
        else:
            print("\nInvalid Account number or login pin.")

    elif user_input == "3":
        break










        # print("\nPlease login with your Account number and Pin.")
        # Acct_no = input("::>")
        # login_pin = input("::>")