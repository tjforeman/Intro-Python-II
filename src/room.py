# Implement a class to hold room information. This should have name and
# description attributes.

# the direction attributes have to have a default value or it causes an error with the constructor 
from item import Item


class Room:
    def __init__(self, name, description, n_to = 0, s_to = 0, e_to = 0, w_to = 0):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.item = []

    def __str__(self):
      s = f'{self.name} {self.description}'
      return s

    def add_items(self, item):
        self.item.append(item)

    def print_item(self):
        print("items in room include: ")
        if len(self.item) > 0:
            for i in self.item:
                print (i.name, i.description)
        else:
            print('there are no items in this room')


    def remove_item(self,item):
        self.item.remove(item)





