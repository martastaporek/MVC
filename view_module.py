from model_module import *
from controler_module import *


def menu():
    """ 
    Function menu() lets the user to call desired module. 
    """

    while True:
        print("1. Add new task")
        print("2. List of task ")
        print("3. List of task with details")
        print("4. Exit")
        answer = input("Enter the number")
        if answer == "1":
            pass
        elif answer == "2":
            pass
        elif answer == "3":
            pass
        elif answer == "4":
            exit()

menu()
