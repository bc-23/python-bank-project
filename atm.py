# your comment here
# your comment here
import os
import csv


global filename, data, raw_data
filename = 'bank250.csv'

f = open(filename, "r")
raw_data = f.read()
raw_data = raw_data.split('\n')
raw_data = list(filter(None, raw_data))


class bank:
    acc_no = 0
    name = ''
    deposite = 0
    acc_type = ''

    def __init__(self):
        self

    def file_write(self, list_data):
        f = open(filename, "w")
        all_data = str()
        for data in list_data:
            all_data += data + '\n'
        f.write(all_data)
        f.close()
        return True

    def account_create(self):
        acc_no = int(input("Enter Account number :"))
        name = input("Enter Account holder name : ")
        deposite = int(input("Enter amount to deposite : "))
        acc_type = input("Enter type of account s/c :")

        data = str(acc_no) + ',' + name + ',' + str(deposite) + ',' + acc_type + ',' + '\n'

        f = open(filename, "a")
        f.write(data)
        f.close()
        print("Account created successfully")

    def account_list(self):
        for data in raw_data:
            split_data = data.split(',')
            print("Account no : ", split_data[0])
            print("Account holder name : ", split_data[1])
            print("Current balance : ", split_data[2])
            print("Account type is : ", split_data[3])
            print('*' * 40)

    def account_modify(self, ac_no):
        print("Account no :", ac_no)
        name = input("Enter Account holder name : ")
        deposite = int(input("Enter amount to deposite : "))
        acc_type = input("Enter type of account s/c :")
        value = str(ac_no) + "," + name + ',' + str(deposite) + ',' + acc_type
        for data in raw_data:
            split_data = data.split(',')
            if ac_no == split_data[0]:
                raw_data[raw_data.index(data)] = value
                self.file_write(raw_data)
                print('Successfully Updated')
                return True
        print('Try Again')

    def deposite(self, ac):
        money = int(input("Enter amount to deposit : "))
        for data in raw_data:
            split_data = data.split(',')
            i = 0
            if ac in split_data[0]:
                base_amount = split_data[2]
                split_data[2] = int(base_amount) + money
                new_col = ''
                for col in split_data:
                    new_col += str(col) + ','
                raw_data[i] = new_col[0:-1]
                if (self.file_write(raw_data)):
                    print('Successfully Deposited amount')
                quit()
            i + 1

    def withdraw(self, ac):
        money = int(input("Enter amount to credit : "))
        for data in raw_data:
            split_data = data.split(',')
            i = 0
            if ac in split_data[0]:
                base_amount = split_data[2]
                split_data[2] = int(base_amount) - money
                new_col = ''
                for col in split_data:
                    new_col += str(col) + ','
                raw_data[i] = new_col[0:-1]
                if (self.file_write(raw_data)):
                    print('Successfully Credited amount')
                quit()
            i + 1

    def account_delete(self, account_number):
        for data in raw_data:
            ac_no = data.split(',')[0]
            if (ac_no == account_number):
                raw_data.remove(data)
                break
        if (self.file_write(raw_data)):
            print('Successfully Delleted !!!!')
        else:
            print('please try again')

    def search_account_no(self, account_no):
        for list_data in raw_data:
            split_data = list_data.split(',')
            if account_no == split_data[0]:
                return True


print("""
	<<<<<<<<<<<<<<<<<Welcome To Bank Management System >>>>>>>>>>>>>>>>>>>>
	1.=Creat Account
	2.=List of Account holders
	3.=Modify Account
	4.=Deposite Amount
	5.=Withdraw Amount
	6.=Delete Account
	7.=Exit
		""")

my_bank = bank()
# my_bank.account_list()

try:
    user_input = int(input("Enter above option for any operation from(1-7) :"))
except ValueError:
    print("\nThat's not true")
else:
    print("\n ")

if user_input == 1:
    my_bank.account_create()


elif user_input == 2:
    my_bank.account_list()


elif user_input == 3:
    num = input("Enter Account number for modification :")
    if my_bank.search_account_no(num):
        my_bank.account_modify(num)
    else:
        print("Incorrect account_no ?????")

elif user_input == 4:
    num1 = input("Enter Account number to deposite amount :")
    if my_bank.search_account_no(num1):
        my_bank.deposite(num1)
    else:
        print("Incorrect account_no ?????")


elif user_input == 5:
    num2 = input("Enter Account number to withdraw amount :")
    if my_bank.search_account_no(num2):
        my_bank.withdraw(num2)
    else:
        print("Incorrect account_no ?????")



elif user_input == 6:
    num3 = input("Enter Account number for delete :")
    f = open(filename, "r")
    raw = f.read()
    if num3 not in raw:
        print("Incorrent Account number????")
    else:
        my_bank.account_delete(num3)

    f.close()

elif user_input == 7:
    print("Thanks for Using Our Bank Management System")
    quit()
else:
    print("Invalid input?????")

my_bank = bank()