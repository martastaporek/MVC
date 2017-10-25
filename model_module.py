class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.done = False

    def mark_item_done(self):
        self.done = True

    def modify_name(self, name):
        self.name = name

    def modify_description(self, description):
        self.description = description

class ItemList:


    item_list = ["testy", ]


    @classmethod
    def add_item(self, name, description):

        item = Item(name, description)
        self.item_list.append(item)

    @classmethod    
    def delete_item(self, number):
        number -= 1 #bo indeksy od 0
        del self.item_list[number]

    def __str__(self):
        return self.item_list