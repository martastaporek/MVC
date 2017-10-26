from model_module import *


def add_item_by_user():
    
    while True:
        name = input("Enter the name of task. Maximum length is 20 characters: ")
        if len(name) < 21:
            break

    while True:
        description = input("Enter the description of the task. Maximum lenght is 150 characters: ")
        if len(description) < 151:
            break

    ItemList.add_item(name, description)


def delete_item_by_user():

    #for i in range(len(ItemList.item_list)): #printowanie tabeli
        #print(ItemList.item_list[1].name)
    
    while True:
        try:
            number = int(input("Enter the number of the task you would like to remove: "))
            break
        except ValueError:
            print("Enter only numbers")
            pass
    
    while True:
        if number < len(ItemList.item_list) + 1:
            break
        else:
            print("The number is not on the list")
            delete_item_by_user()

    ItemList.delete_item(number)





