"""
This file contains the item class
"""

class Item:
    """
    Item Class with no methods
    """
    def __init__(self, name="Heart_1", description="Healing Item", item_type="Heart"):
        self.name = name # Heart, Arrow, or Key followed by a number
        self.description = description # Healing Item, Ranged Weapon Ammo, or Tool for Opening Doors
        self.item_type = item_type # Heart, Arrow, or Key