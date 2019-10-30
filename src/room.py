# Implement a class to hold room information. This should have name and
# description attributes.

# the direction attributes have to have a default value or it causes an error with the constructor 
class Room:
    def __init__(self, name, description, n_to = 0, s_to = 0, e_to = 0, w_to = 0):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
      s = f'{self.name} {self.description}'
      return s
