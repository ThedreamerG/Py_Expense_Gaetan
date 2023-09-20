from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense,CreateNewUser, Add_all_spenders, show_status
import os.path

pathExpenses = 'Expenses.csv'
pathUsers = 'Users.csv'

def createCSVExpenses():
    csv = open("Expenses.csv", "w")
    csv.write("Amount,Label,Spender,paybac\n")
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
    elif (option['main_options']) == "New User":
        CreateNewUser()
        ask_option()
    elif (option['main_options']) == "Show Status":
        show_status()
        ask_option()

def main():
    check_file_Expense = os.path.isfile(pathExpenses)
    check_file_Users = os.path.isfile(pathUsers)
    if (not check_file_Expense):
        createCSVExpenses()
    if (not check_file_Users):
        createCSVUsers()
    else :	
        Add_all_spenders()
    ask_option()

main()