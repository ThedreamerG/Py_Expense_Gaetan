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
            if len(answer) == 0  or answer == answer[0] else True
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
    # clean by removing the last 'new line' character
    spender = infos["spender"].replace("\n", "")
    payback = [user.replace("\n", "") for user in infos["payback"]]

    # Check if the amount is a number
    if (not check_if_number(amount)):
        return False
    
    if (UsersList == []):
        Add_all_spenders()
    # Spender is in the list of users
    csv = open("Expenses.csv", "a")
    csv.write(amount + "," + label + "," + spender + "," + str(payback).replace(", ","-") + "\n")
    csv.close()
    # Add the new expense to the list of expenses
    return True	

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    if (add_expense(infos)) :
        print("Expense Added")
    else :
        print("Failure!!")
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
    Users.clear()
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
    Expense.clear()
    csv = open("Expenses.csv", "r")
    csv.readline() # Skip the first line (header)
    # read the last element as a list
    for line in csv:
        [amount, label, spender, payback] = line.split(",")
        # extract the paybacks ['ewq'-'zxc'] -> ['ewq','zxc'] and remove the new line character
        paybacks = payback.replace("[","").replace("]","").replace("'","").split("-")
        paybacks = [user.replace("\n", "") for user in paybacks]
        Expense.append([amount, label, spender, paybacks])
    csv.close()
    print(Expense)

def check_if_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
    
def show_status():
    print("Show Status")
    Add_all_expenses()
    OptimizedExpense = []
    ## add the amount of each expense to the spender for each payback user
    for expense in Expense:
        [amount, label, spender, payback] = expense
        for user in payback:
            # check if the user is the spender
            if (user == spender):
                continue
            # check if the user already has an optimized expense
            for optimizedExpense in OptimizedExpense:
                if (optimizedExpense[1] == user and optimizedExpense[2] == spender):
                    optimizedExpense[0] += float(amount)/len(payback)
                    break
            else:
                OptimizedExpense.append([float(amount)/len(payback), user, spender])
    # show the optimized expenses
    for optimizedExpense in OptimizedExpense:
        print(optimizedExpense[1] + " owes " + optimizedExpense[2] + " " + str(optimizedExpense[0] + "$"))      
    return True
    
