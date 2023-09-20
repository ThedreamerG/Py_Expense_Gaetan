from PyInquirer import prompt
import os.path
pathExpenses = './Expenses.csv'
pathUsers = './Users.csv'

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
]

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]


def add_expense(infos):
    amount = infos["amount"]
    label = infos["label"]
    spender = infos["spender"]
    csv = open("Expenses.csv", "a")
    csv.write(amount + "," + label + "," + spender + "\n")
    csv.close()


def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    add_expense(infos)
    print("Expense Added !")
    return True


def CreateNewUser(*args):
    print("Create New User")
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea (╯°□°)╯︵ ┻━┻
    user_name = infos["name"]
    csv = open("Users.csv", "a")
    csv.write(user_name + "\n")
    return True
