import sys
import os.path
folder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(folder)
# Import your functions

from rpg.enemy import Enemy, Skeleton  # noqa: E402
from rpg.player import Player  # noqa: E402

if __name__ == "__main__":
    # arty = Enemy("Arty")
    # print(arty.health)
    # arty.health = 200
    # print(Enemy.health.__doc__)

    skeleton = Skeleton(5)
    