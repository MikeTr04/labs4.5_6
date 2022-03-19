"""MAIN GAME MODULE"""

"""Score represents the number of enemies that the
player has beaten already."""
score = 0


class Room:
  """Room class"""
  def __init__(self, name):
    """Initializes a room with given attribute name
    and desctiption, link, character, item as None,
    neighbors as a map with 4 keys corresponding to
    directions (north, east, south, west) and their
    values None."""
    self._name = name
    self._description = None
    self._link = None
    self._character = None
    self._item = None
    self._neighbors = {"north": None, "east" : None, "south" : None, "west" : None}
  
  def set_description(self, description):
    """Setter for the description."""
    self._description = description
  
  def get_details(self):
    """Getter for the description."""
    print(self._description)
    
  def link_room(self, room, direction):
    """Adds a value to a key in neighbors by direction."""
    self._neighbors[direction] = room
  
  def set_character(self, character):
    """Sets character in the room."""
    self._character = character
    
  def get_character(self):
    """Getter for the character in the room."""
    return self._character
  
  def set_item(self, item):
    """Setter for the item in the room."""
    self._item = item
    
  def get_item(self):
    """Getter for the item in the room."""
    return self._item
  
  def move(self, direction):
    """Returns the neighboring room in the direction."""
    if self._neighbors[direction] is not None:
      return self._neighbors[direction]
    else:
      print("No neighbors for direction")
      return self

  
class Enemy:
  """Enemy class"""
  def __init__(self, name, description):
    """Initializes an enemy by name and description,
    as well as weakness, conversation as None and defeated_cnt
    as score."""
    self._name = name
    self._description = description
    self._weakness = None
    self._conversation = None
    self._defeated_cnt = score
  
  def set_weakness(self, weakness):
    """Setter for the weakness."""
    self._weakness = weakness
  
  def set_conversation(self, conversation):
    """Setter for the conversation."""
    self._conversation = conversation
  
  def talk(self):
    """Prints conversation."""
    print(self._conversation)
  
  def describe(self):
    """Prints conversation."""
    print(self._description)
  
  def fight(self, item):
    """
    A function that represents a fight.
    If the item that the player uses to attack is a
    weakness of the enemy, the enemy dies.
    Returns True and increases the score by 1 if
    the player wins, or returns False if the player
    loses.
    >>> enemy = Enemy("Dave", "whatever")
    >>> enemy.set_weakness("cheese")
    >>> enemy.fight("cheese")
    True
    >>> enemy = Enemy("Dave", "whatever")
    >>> enemy.set_weakness("cheese")
    >>> enemy.fight("book")
    True
    """
    if self._weakness == item:
      global score
      score += 1
      return True
    return False
    
  def get_defeated(self):
    """Gets the current score of defeated enemies
    and returns it."""
    self._defeated_cnt = score
    return self._defeated_cnt


class Ally:
  """Ally class"""
  def __init__(self, name, description):
    """Initializes an ally with name and description,
    and conversation as None."""
    self._name = name
    self._description = description
    self._conversation = None
  
  def set_conversation(self, conversation):
    """Setter for the conversation."""
    self._conversation = conversation
  
  def talk(self):
    """Prints the conversation"""
    print(self._conversation)
  
  def describe(self):
    """Prints the description."""
    print(self._description)

    
class Item:
  """Item class"""
  def __init__(self, name):
    """Initializes the item by name, and description as None."""
    self._name = name
    self._description = None
  
  def get_name(self):
    """Getter for the name of the item."""
    return self._name
  
  def set_description(self, description):
    """Setter for the description of the item."""
    self._description = description
  
  def describe(self):
    """Prints the description."""
    print(self._description)
  