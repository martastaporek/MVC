from model_module import *
from controller_module import *


def menu():
    """ 
    Function menu() lets the user to call desired module. 
    """

    while True:
        print("1. Add new task")
        print("2. List of task ")
        print("3. List of task with details")
        print("4. Delete task")
        print("5. Change the name of the task")
        print("6. Change the description of the task")
        print("7. Change the status of the task to done")
        print("8. Exit")
        answer = input("Enter the number: ")
        if answer == "1":
            add_item_by_user()
        elif answer == "2":
            print(ItemList.basic_data_to_print())
        elif answer == "3":
            print(ItemList.specific_data_to_print())
        elif answer == "4":
            delete_item_by_user()
        elif answer == "5":
            change_name()
        elif answer == "6":
            change_description()
        elif answer == "7":
            mark_as_done()
        elif answer == "8":
            exit()

if __name__ == "__main__":
    
    ItemList.add_item("task1", "test description")
    menu()
