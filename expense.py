from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "validate": lambda result: inList(result) or "User should be in the list added"
    },

]

expense_questions2 = [
    {
        "type": "input",
        "name": "name",
        "message": "New Expense - user in spending type no for no new spender: ",
        "validate": lambda result: inList(result) or result == "no" or "User should be in the list"
    }
]

header = ['amount', 'label', 'spender']


def inList(user):
    file = open('users.csv', 'r')
    reader = csv.reader(file)
    for i in reader:
        # print(i[0])
        if user == i[0]:
            return True
    return False


def new_expense(*args):
    infos = prompt(expense_questions)

    data = [infos['amount'], infos['label'], infos['spender']]
    infos_spender = prompt(
        expense_questions2, validate=lambda result: len(result) > 0)
    while (infos_spender['name'] != "no"):
        data.append(infos_spender['name'])
        infos_spender = prompt(
            expense_questions2, validate=lambda result: len(result) > 0)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    f = open('expense_report.csv', 'a')
    writer = csv.writer(f)
    # writer.writerow(header)
    writer.writerow(data)
    print("Expense Added !")
    return True
