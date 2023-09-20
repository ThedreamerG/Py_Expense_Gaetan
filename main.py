from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
import os.path

pathExpenses = './Expenses.csv'
pathUsers = './Users.csv'

def createCSVExpenses():
    csv = open("Expenses.csv", "w")
    csv.write("Amount,Label,Spender\n")
    csv.close()
def createCSVUsers():
    csv = open("Users.csv", "w")
    csv.write("Name\n")
    csv.close()


def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()

def main():
    check_file_Expense = os.pathExpenses.isfile(pathExpenses)
    check_file_Users = os.pathUsers.isfile(pathUsers)

    if (check_file_Expense):
        csv = open("Expenses.csv", "x")
    else:
        createCSVExpenses()
    if (check_file_Users):
        csv = open("Users.csv", "x")
    else:
        createCSVUsers()
    ask_option()

main()