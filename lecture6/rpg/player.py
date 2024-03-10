"""
This file contains the player class.
"""

import random
from item_found import Item

class Player:
    def __init__(self, name="Hero", health=100, inventory = [0, 0]):
        self.name = name
        self.health = health
        self.inventory = inventory # the number of arrows if the first item and the secons item is the number of keys

    def __str__(self):
        return f"{self.name} has {self.health} health.\nThere are {self.inventory[0]} arrow(s) and {self.inventory[1]} key(s) in inventory."

    def __iter__(self):
        return iter([self.name, self.health])

    def __contains__(self, item):
        return item in (self.name, self.health)

    def __call__(self, amount):
        if amount > 0:
            self.health += amount
            print(f"{self.name} is healed by {amount} health points.")
        else:
            print("Invalid healing amount. Please provide a positive integer.")

    def __gt__(self, other):
        if isinstance(other, Player):
            return self.health > other.health
        else:
            raise TypeError("Unsupported operand types for >")

    def __add__(self, other):
        if isinstance(other, int):
            return Player(self.name, self.health + other)
        elif isinstance(other, Player):
            return Player(f"{self.name+other.name}", self.health + other.health)
        else:
            raise TypeError("Unsupported operand types for +")

    def attack(self, enemy, damage):
        """
        Attack the enemy.

        Args:
            enemy (Enemy): The enemy to attack.
            damage (int): The amount of damage to deal.
        """
        print(f"🤴🗡️ {self.name} attacks {enemy.name}!")
        enemy.take_damage(damage)

    def defend(self):
        """
        Defend against an attack.
        """
        print(f"🤴🛡️ {self.name} defends!")

    def take_damage(self, damage):
        """
        Take damage from an attack.

        Use random to determine if the player will defend or take damage.
        50% chance to defend, 50% chance to take damage.


        Args:
            damage (int): The amount of damage to take.
        """
        # create a random number between 0 and 1
        # if the number is greater than 0.5, the player will defend
        # if the number is less than 0.5, the player will take damage
        if random.random() > 0.5:
            self.defend()
        else:
            self.health -= damage
            if self.health <= 0:
                print(f"🤴💀 {self.name} has been defeated!")
            else:
                print(f"🤴💚 {self.name} has {self.health} health left.")
                
    def pick_up(self, item_found):
        """
        Pick up the object that was found.
        
        Add health if it is a heart.
        Add an item to either inventory slot if it is an arrow or key
        
        Args:
            item_found (class item): either a heart, arrow, or key with corresponding name, description, and item_type
        """
        # first add health, then inventory
        if (item_found.item_type == "Heart"):
            self.health += 10
        elif (item_found.item_type == "Arrow"):
            self.inventory[0] += 1
        elif (item_found.item_type == "Key"):
            self.inventory[1] += 1
            
    def remove_item(self, item_remove):
        """
        Remove the object that was prompted.
        
        Remove health if it is a heart.  This could be called damage, but I am keeping it simple
        Remove an item from either inventory slot if it is an arrow or key
        
        Args:
            item_found (class item): either a heart, arrow, or key with corresponding name, description, and item_type
        """
        if (item_remove.item_type == "Heart"):
            self.health -= 10
        elif (item_remove.item_type == "Arrow"):
            self.inventory[0] -= 1
        elif (item_remove.item_type == "Key"):
            self.inventory[1] -= 1

if __name__ == "__main__":
    # create the player
    arthur = Player("Arthur")
    
    # create each item type for the test
    heart_test = Item("Heart1", "Healing Item", "Heart")
    arrow_test = Item("Arrow1", "Ranged Weapon Ammo", "Arrow")
    key_test =Item("Key1", "Tool for Opening Doors", "Key")
    
    # pick up each item type
    arthur.pick_up(heart_test)
    arthur.pick_up(arrow_test)
    arthur.pick_up(key_test)
    
    # print the results
    print(arthur.__str__())
    
    # remove each item type
    arthur.remove_item(heart_test)
    arthur.remove_item(arrow_test)
    arthur.remove_item(key_test)
    
    # print the results
    print(arthur.__str__())