class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.done = False

class ItemList:

    item_list = []

    def __init__(self, item_list):
        self.item_list = item_list

    @classmethod
    def add_item(self, name, description):
        item = Item(name, description)
        self.item_list.append(item)

    @classmethod    
    def delete_item(self, number):
        number -= number
        del self.item_list[number]

    @classmethod
    def basic_data_to_print(self):
        basic_date = ""
        for i in range(len(self.item_list)):
            item = str(i+1) + " | " + self.item_list[i].name
            basic_date += item + "\n"

        return basic_date
            
    @classmethod
    def specific_data_to_print(self):
        specific_data = ""
        is_done = ""
        for i in range(len(self.item_list)):
            if self.item_list[i].done is True:
                is_done = "done"
            else:
                is_done = "to do"
            item = str(i+1) + " | " + self.item_list[i].name + " | " + self.item_list[i].description + " | " + is_done
            specific_data += item + "\n"

        return specific_data

    def __str__(self):
        return self.item_list




