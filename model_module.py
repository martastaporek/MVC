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
    