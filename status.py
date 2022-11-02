from PyInquirer import prompt
import csv


def initData():
    data = []
    file = open('users.csv', 'r')
    reader = csv.reader(file)
    for i in reader:
        data.append((i[0], 0))
        putMoney(data, i[0])
    return data


def inList(reader, user):
    for i in reader:
        # print(i)
        if user == i:
            return True
    return False


def putMoney(data, user):
    res = data
    f = open('expense_report.csv', 'r')
    reader = csv.reader(f)
    for i in reader:
        money = i[0]
        val = int(money) / (len(i) - 2)
        if (i[2] == user):
            (a, b) = data[-1]
            data[-1] = (a, b + val)
        else:
            if (inList(i, user)):
                (a, b) = data[-1]
                data[-1] = (a, b - val)
    return data


def findMax(data):
    max = ("name", 0)
    for i in data:
        (a, b) = i
        (c, d) = max
        if b > d:
            max = (a, b)
    return max


def show_status():
    # This function should create a new user, asking for its name
    f = open('expense_report.csv', 'r')
    reader = csv.reader(f)
    data = initData()
    (max, name) = findMax(data)
    for i in data:
        (a, b) = i
        if max == b:
            print("user " + b + " owes nothing")
        else:
            print("user " + b + " owes " + a +
                  " to the man that is " + name)
    return True
