from PyInquirer import prompt
import os.path
pathExpenses = './Expenses.csv'
pathUsers = './Users.csv'

Users = []
Expense = []
UsersList = []


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
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender(s): ",
        "choices": UsersList,
    },
    {
        "type":"checkbox",
        'qmark': '😃',
        "name":"payback",
        "message":"New Expense - PayBack(s): ",
        "choices": UsersList,
        "validate": lambda answer: 'You must choose at least one topping and different from the user choosen.' \
            if len(answer) == 0 else True
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
    payback = infos["payback"]

    # Check if the amount is a number
    if (not check_if_number(amount)):
        return False
    
    if (UsersList == []):
        Add_all_spenders()
    # spender is in the list of users
    csv = open("Expenses.csv", "a")
    csv.write(amount + "," + label + "," + spender + "," + str(payback))
    csv.close()
    # Add the new expense to the list of expenses
    return True	


def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    add_expense(infos)
    print("Expense Added !")
    return True


def CreateNewUser(*args):
    print("Create New User")
    infos = prompt(user_questions)
    # Writing the informations on external file might be a good idea (╯°□°)╯︵ ┻━┻
    user_name = infos["name"]
    csv = open("Users.csv", "a")
    csv.write(user_name + "\n")
    csv.close()
    print("User Added !")
    # Add the new user to the list of users
    Users.append(user_name)
    UsersList.append(
        {
            "name":user_name
        }
    )
    return True

def Add_all_spenders():
    csv = open("Users.csv", "r")
    csv.readline() # Skip the first line (header)
    for line in csv:
        Users.append(line)
        UsersList.append(
            {
                "name": line
            }
        )
    csv.close()

def Add_all_expenses():
    csv = open("Expenses.csv", "r")
    csv.readline() # Skip the first line (header)
    for line in csv:
        [amount, label, spender, payback] = line.split(",")
        Expense.append([amount, label, spender, payback])
    csv.close()

def check_if_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False