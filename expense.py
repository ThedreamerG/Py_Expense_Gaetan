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
        "name":"spenders",
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
    spenders = infos["spenders"]
    payback = infos["payback"]
    if (UsersList == []):
        Add_all_spenders()
    # spender is in the list of users
    csv = open("Expenses.csv", "a")

    csv.write(str(money_per_spender) + "," + label + "," + spender)
        
    csv.close()
    # Add the new expense to the list of expenses
    for spender in spenders:
        Expense.append([money_per_spender, label, spender])
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
        [amount, label, spender] = line.split(",")
        Expense.append([amount, label, spender])
    csv.close()
