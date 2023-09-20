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


def createCSV():
    csv = open("Expenses.csv", "w")
    csv.write("Amount,Label,Spender\n")
    csv.close()

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
    print(infos)

    check_file = os.path.isfile(path)
    if (check_file):
        csv = open("Expenses.csv", "x")
    else:
        createCSV()
    add_expense(infos)
    print("Expense Added !")
    return True


