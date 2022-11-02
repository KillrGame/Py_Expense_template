from PyInquirer import prompt
import csv


def initData():
    data = []
    file = open('users.csv', 'r')
    reader = csv.reader(file)
    for i in reader:
        data.append([i[0], 0])
    return data


def putMoney(data):
    res = data
    f = open('expense_report.csv', 'r')
    reader = csv.reader(f)
    for i in reader:
        print(i[0])
    return data


def show_status():
    # This function should create a new user, asking for its name
    print("hello")
    f = open('expense_report.csv', 'r')
    reader = csv.reader(f)
    data = initData()
    putMoney(data)
    return True
