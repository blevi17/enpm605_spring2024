"""
This module contains the maze and the robot's initial position, as well as functions to print the maze and move the robot.
"""
from typing import List

# Constants
# Here are all the emojis: "💥", "🏁", "⏫", "⏩", "⏪", "⏬", "🚧"
EMPTY = "  "
BOOM = "💥"
OBSTACLE = "🚧"
GOAL = "🏁"
ROBOT = "⏫"
HORIZONTAL_WALL = "──"
VERTICAL_WALL = "│"
CORNER = "┼"

# Define the size of the maze
MAZE_SIZE = 4

# Define the maze as a 2D list
maze = [[EMPTY] * MAZE_SIZE for _ in range(MAZE_SIZE)]
# Rewrite the previous line using for loops


# Define the robot's initial position
robot_position = [2, 3]  # [row, column]
robot_orientation = "up"

# Define the obstacles' positions
obstacle_positions = [[1, 1], [2, 2], [3, 3]]

# Define the goal position
goal_position = [3, 2]

# Place obstacles, the robot, and the goal in the maze
for obstacle in obstacle_positions:
    maze[obstacle[0]][obstacle[1]] = OBSTACLE

# maze[robot_position[0]][robot_position[1]] = ROBOT
maze[goal_position[0]][goal_position[1]] = GOAL

def update_robot_arrow(orien_arr: str) -> str:
    '''update_robot_arrow produce the robot as an arrow

    This produces the arrow facing the correct orientation based on the orientaion as a string

    Args:
        orien_arr (str): orientation of the robot: up, down, left, right

    Returns:
        str: orientation of the robot in emoji form
    '''
    if (orien_arr == "up"):
        arrow = "⏫"
    elif (orien_arr == "down"):
        arrow = "⏬"
    elif (orien_arr == "left"):
        arrow = "⏪"
    elif (orien_arr == "right"):
        arrow = "⏩"
    else:
        print("The robot was arrow was not updated") 
        arrow =  "⏫"
    
    return arrow      

# Function to print the maze
def print_maze(robot_position_m: List[int], robot_orientation_m: str):
    '''print_maze print a a 4 by 4 space with a goal and obstacles

    This function prints aout a spaces with rectangles in a 4 by 4 pattern.
    There are 3 obstacles and one goal. There is a robot represented by an arrow

    Args:
        robot_position_m (List[int]): position of the robot in x-y coordinates (top left is the origin)
        robot_orientation_m (str): the orientation of the robot: up, down, left, right
    '''
    
    # Print top boundary
    print("┌" + "─" * (MAZE_SIZE * 3 - 1) + "┐")
    
    # Get the robot arrow and update it
    robot_arrow = update_robot_arrow(robot_orientation_m)
    maze[robot_position_m[0]][robot_position_m[1]] = robot_arrow
    
    for i, row in enumerate(maze):
        # Print left boundary
        print(VERTICAL_WALL, end="")

        # Print cell contents
        for j, cell in enumerate(row):
            print(cell, end="")
            # Print vertical wall if not in the last column
            if j < MAZE_SIZE - 1:
                print(VERTICAL_WALL, end="")

        # Print right boundary
        print(VERTICAL_WALL)

        # Print horizontal wall between rows (except for the last row)
        if i < MAZE_SIZE - 1:
            print("├" + "─" * (MAZE_SIZE * 3 - 1) + "┤")

    # Print bottom boundary
    print("└" + "─" * (MAZE_SIZE * 3 - 1) + "┘")
    
    # check if you are at the finish
    if (robot_position_m == goal_position):
        print("You have successfully reached the end!")
        quit()
    
    # Make the space blank to delete the old robot
    maze[robot_position_m[0]][robot_position_m[1]] = "  "

if __name__ == "__main__":
    print_maze()