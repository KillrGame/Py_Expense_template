from PyInquirer import prompt
import csv

user_questions = [{

    "type": "input",
    "name": "name",
    "message": "New User - name is: ",
},
]


def add_user():
    infos = prompt(user_questions, validate=lambda result: len(result) > 0)
    # This function should create a new user, asking for its name

    f = open('users.csv', 'a')
    writer = csv.writer(f)
    data = [infos['name']]
    writer.writerow(data)
    print("User Added !")
    return True
