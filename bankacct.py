import csv
import os
global filename, data, raw_data
filename='bank250.csv'

f = open(filename, "r")
raw_data = f.read()
raw_data = raw_data.split('\n')
raw_data = list(filter(None, raw_data))


def file_write(self, list_data):
    f1 = open(filename, "w")
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
        self.cust_acc_num = BankAccount.acc_num
        self.mobile_no = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin

        BankAccount.acc_num = BankAccount.acc_num + 1
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1

    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: ${self.acc_balance}')

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            data1 = os.name + ',' + str(self.mobile_no) + ',' + str(self.acc_balance) + ',' + str(self.pin) + '\n'
            f1 = open(filename, "a")
            f1.write(data1)
            f1.close()
            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if self.acc_balance >= amount > 0:
            self.acc_balance = self.acc_balance - amount
            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def payment(self, other):
        amount = int(input('Enter the payment amount: '))
        if self.acc_balance >= amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')


if __name__ == '__main__':
    cust1 = BankAccount(name='Alex', mobile_no=4808435553, initial_depo=1000, pin=1234)
    cust2 = BankAccount(name='Betty', mobile_no=4808435553, initial_depo=2000, pin=1234)
    print('No. of customers is', BankAccount.no_of_cust)
    print(cust1.basic_details())
    print(cust2.basic_details())
    # cust1.deposit()
    # print(cust1.basic_details())
    # cust1.withdrawl()
    # print(cust1.basic_details())
    cust1.payment(cust2)
    print(cust2.basic_details())

