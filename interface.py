from bankacct import BankAccount

import csv
import os
global file, data, raw_data, f
file='bank250.csv'


f = open(file, "r")
raw_data = f.read()
raw_data = raw_data.split('\n')
raw_data = list(filter(None, raw_data))
customer_dict = {}  # use account no. as key and class object(customer account) as value
mobile_acc_link = {}  # use mobile no. as key and store account no. as value, for linking purpose


def new_cust():
    f1 = None

    name = input('Enter the name of customer: ')

    try:
        mobile_no = int(input('Enter the mobile number of customer: '))
    except ValueError:
        print("Invalid number")
    try:
        initial_depo = int(input('Enter the initial deposit amount: '))

    except ValueError:
        print("Invalid amount")

    if initial_depo <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)
    customer_dict[customer.cust_acc_num] = customer  # acct. no. stored as key and object as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num  # mobile no. linked
    data1 = name+','+str(mobile_no)+','+str(initial_depo)+','+str(pin)+'\n'
    with open(file, 'a') as f1:
        f1.write(data1)

    # try:
    #     f1 = open(file, 'a')
    #     f1.write(data1)
    #
    # finally:
    #
    #     if file:
    #         f1.close()
    print('New User Created!')
    print(f'Welcome {customer.name} to Hometown Bank.\n{customer.cust_acc_num} is your account number')


def login():
    account_no = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin:
        print(f'\n{customer_dict[account_no].name} Logged in')
        customer_dict[account_no].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input('''Press 1 for deposit:
            Press 2 for withdrawl:
            Press 3 for money transfer:
            Press 4 to log out\n''')
        if user_input1 == '1':
            customer_dict[account_no].deposit()
        elif user_input1 == '2':
            customer_dict[account_no].withdrawl()
        elif user_input1 == '3':
            mobile = int(input('Enter account holder cell phone number: '))
            if mobile in mobile_acc_link.keys():
                secondary = mobile_acc_link[mobile]  # use mobile no. to get acct. no.
                customer_dict[account_no].payment(customer_dict[secondary])
            else:
                print('The phone number entered is not associated with any account.')
        elif user_input1 == '4':
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        print('\n#############################################################\n')
        customer_dict[account_no].basic_details()


while True:
    user_input1 = input('''Press 1 if you are a new customer:
Press 2 if you are logging in as an existing customer:
Press 3 to display number of customers currently signed on:
Press 4 to exit\n''')

    if user_input1 == '1':
        print('Create user')
        new_cust()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print(''
              'There currently', BankAccount.no_of_cust, 'customers in the bank.')
    elif user_input1 == '4':
        print('Exited')
        break
    else:
        print('Invalid input try again')
    print('\n*************************************************************\n')
