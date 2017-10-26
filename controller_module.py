from model_module import *

def enter_the_name_of_task():  
    while True:
        name = input("Enter the name of task. Maximum length is 20 characters: ")
        if len(name) < 21 or len(name) == 0:
            return name


def enter_the_description_of_task():
    while True:
        description = input("Enter the description of the task. Maximum lenght is 150 characters: ")
        if len(description) < 151 or len(description) == 0:
            return description

def add_item_by_user():
    name = enter_the_name_of_task()
    description = enter_the_description_of_task()
    ItemList.add_item(name, description)

    
def choose_task_by_number():   
    while True:
        try:
            number = int(input("Enter the number of the task: "))
            break
        except ValueError:
            print("Enter only numbers")
            pass
    
    while True:
        if number < len(ItemList.item_list) + 1 and number > 0:
            break
        else:
            print("The number is not on the list")
            delete_item_by_user()
    
    return number

def delete_item_by_user():
    print(ItemList.basic_data_to_print())
    print("Here you can choose which task to remove.")
    number = choose_task_by_number()
    ItemList.delete_item(number)   


def print_list():
    print(ItemList.basic_data_to_print())


def print_specific_list():
    print(ItemList.specific_data_to_print())

def choose_task_to_change():
    print(ItemList.specific_data_to_print())
    number = choose_task_by_number()
    task = ItemList.item_list[number - 1]

    return task

def change_name():
    task = choose_task_to_change()
    name = enter_the_name_of_task()
    task.name = name

def change_description():
    task = choose_task_to_change()
    description = enter_the_description_of_task()
    task.description = description

def mark_as_done():
    task = choose_task_to_change()
    task.done = True







