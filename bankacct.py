import csv
import os
global file, data, raw_data
file = 'bank250.csv'

f = open(file, "r")
raw_data = f.read()
raw_data = raw_data.split('\n')
raw_data = list(filter(None, raw_data))


def file_write(self, list_data):
    f1 = open(file, "w")
    all_data = str()
    for data1 in list_data:
        all_data += data1+'\n'
    f1.write(all_data)
    f1.close()
    return True


class BankAccount:
    no_of_cust = 0
    acc_num = 42010

    def __init__(self, name, mobile_no, initial_depo, pin):

        self.name = name
        self.mobile_no = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin

        self.cust_acc_num = BankAccount.acc_num

        BankAccount.acc_num = BankAccount.acc_num + 1
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1

        #  The method below is called whenever a user is logged in

    def basic_details(self):
        print(f'User: {self.name}\nAccount No: {self.cust_acc_num}\nBalance: ${self.acc_balance}')

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            data1 = self.name + ',' + str(self.mobile_no) + ',' + str(self.acc_balance) + ',' + str(self.pin) + '\n'
            f1 = open(file, "a")
            f1.write(data1)

            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
            print('============================================================')
            f1.close()
        else:
            print('Invalid amount transaction aborted')
    # line 58 makes sure there is enough money in the account for withdraw
    # line 59 updates the balance after withdrawl

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if self.acc_balance >= amount > 0:
            self.acc_balance = self.acc_balance - amount
            data1 = self.name + ',' + str(self.mobile_no) + ',' + str(self.acc_balance) + ',' + str(self.pin) + '\n'
            with open(file, 'a') as f1:
                f1.write(data1)
            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
            print('============================================================')
        else:
            print('Invalid amount transaction aborted')

    # line 72 makes sure deposit is a valid positive number
    # line 73 updates the balance after deposit

    def transfer(self, other):
        amount = int(input('Enter the payment amount: '))
        if self.acc_balance >= amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            data1 = self.name + ',' + str(self.mobile_no) + ',' + str(self.acc_balance) + ',' + str(self.pin) + '\n'
            with open(file, 'a') as f1:
                f1.write(data1)
            print(f'Transaction completed. Your current Balance: ${self.acc_balance}\n')

            print(f'Transaction completed. Recipient Balance: ${other.acc_balance}\n')
            print('============================================================')
        else:
            print('Invalid amount transaction aborted')


if __name__ == '__main__':
    cust1 = BankAccount(name='Alex', mobile_no=4808435553, initial_depo=1000, pin=1234)

    print('No. of customers is', BankAccount.no_of_cust)
    print(cust1.basic_details())

    cust1.deposit()
    print(cust1.basic_details())

    cust1.withdrawl()
    print(cust1.basic_details())

    # cust1.transfer(cust2)
    print(cust1.basic_details())

