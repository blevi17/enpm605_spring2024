"""
This is the main file which contains the entry point of your program.
"""

from maze import print_maze
from robot import update_robot
import maze


def main():
    '''main this program moves a robot through a 4 by 4 spacewith obtacles

    This program mpves the robot though a 4 by 4 space while staying the space and not hitting obstacles.
    The robot moves with tank controls. It can only move forward and backwards or rotate 90 degrees in either direction.
    Once the robot reaches the goal the program stops, or the user can quit by pressing q.
    '''
    
    # Bring in the orientation and position of the robot with the obstacle positions as well
    rob_orient = maze.robot_orientation
    rob_pos = maze.robot_position
    obs_pos = maze.obstacle_positions
    
    # Print the initial maze
    print("Initial Maze:")
    print_maze(rob_pos, rob_orient)
    while True:
        # Collect user input
        action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")
        
        # Update the robot if it can move the way the user asked
        rob_pos, rob_orient = update_robot(action, rob_orient, rob_pos, obs_pos)
        
        # Print the maze
        print_maze(rob_pos, rob_orient)


# Run the main function
if __name__ == "__main__":
    main()
