from PyInquirer import prompt
import os.path
path = './Expenses.csv'

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



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print(infos)

    check_file = os.path.isfile(path)
    if (check_file):
        csv = 

    csv = open("Expenses.csv", "a")

    # con
    print("Expense Added !")
    return True


