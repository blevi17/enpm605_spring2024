"""
This module contains the functions that control the robot's movement.
"""
from typing import List
from copy import deepcopy

def check_target(pos_c: List[int], obs_c: List[List[int]]) -> bool:
    '''check_target this function checks is a robot can move to a location

    this function checks if the position a robot is moving towards is in the workplace or an obstacle to determine if the robot can move there

    Args:
        pos_c (List[int]): the new position the robot is potentially traveling to
        obs_c (a list of a list of ints): a list of the obstacle locations, e.g.: [[1, 1], [2, 2], [3, 3]]

    Returns:
        bool: false means the robot cannot move to a location, and true means a robot can move to a location
    '''
    
    # Start with the assumption the robot can move
    movable = True
    
    # check if the target position is in the workspace
    if pos_c[0] > 3 or pos_c[0] < 0 or pos_c[1] > 3 or pos_c[1] < 0:
        movable = False
        print("Hit a boundary!")
    
    # check if the target space is an obstacle
    for obs in obs_c:
        if (obs == pos_c):
            movable = False
            print("Hit an obstacle!")
            quit()
    
    return movable


def move_forward(orien_f: str, pos_f: List[int], obs_f: List[List[int]]) -> List[int]:
    '''move_forward this program moves the robot forward if possible

    this program moves the robot forward based on orientation, and checks if the robot can move to the position before returning the new location

    Args:
        orien_f (str): the orientation of the robot
        pos_f (List[int]): the position of the robot before moving forward
        obs_f (List[List[int]]): list of positions for the obstacles

    Returns:
        List[int]: the position of the robot after moving, if movement was possible
    '''
    # change the position based on orientation
    pos_fn = deepcopy(pos_f)
    if (orien_f == "up"):
        pos_fn[0] -= 1
    elif (orien_f == "down"):
        pos_fn[0] += 1
    elif (orien_f == "left"):
        pos_fn[1] -= 1
    elif (orien_f == "right"):
        pos_fn[1] += 1
    else:
        print("Position was not changed due to improper input")
    
    # check if the change position is appropiate before returning the value
    if check_target(pos_fn, obs_f):
        pos_fnr = deepcopy(pos_fn)
    else:
        pos_fnr = deepcopy(pos_f)
        
    return pos_fnr


def move_backward(orien_b: str, pos_b: List[int], obs_b: List[List[int]]) -> List[int]:
    '''move_backward this program moves the robot down if possible

    this program moves the robot back based on orientation, and checks if the robot can move to the position before returning the new location

    Args:
        orien_b (str): the orientation of the robot
        pos_b (List[int]): the position of the robot before moving back
        obs_b (List[List[int]]): list of positions for the obstacles

    Returns:
        List[int]: the position of the robot after moving, if movement was possible
    '''
    # change the position
    pos_bn = deepcopy(pos_b)
    if (orien_b == "up"):
        pos_bn[0] += 1
    elif (orien_b == "down"):
        pos_bn[0] -= 1
    elif (orien_b == "left"):
        pos_bn[1] += 1
    elif (orien_b == "right"):
        pos_bn[1] -= 1
    else:
        print("Position was not changed due to improper input")
        
    # check if the change position is appropiate before returning the value
    if check_target(pos_bn, obs_b):
        pos_bnr = deepcopy(pos_bn)
    else:
        pos_bnr = deepcopy(pos_b)
        
    return pos_bnr


def turn_left(orien_l: str) -> str:
    '''turn_left changes the orientation or the robot by turning left

    this function takes in an orientation as a string and outputs a new orientation based on the original

    Args:
        orien_l (str): the original robot orientation before the function was called

    Returns:
        str: the new robot orientation after turning left
    '''
    # Sart with the orienation not changing
    orien_ln = orien_l
    
    # determine the current orientation then turn
    if (orien_l == "up"):
        orien_ln = "left"
    elif (orien_l == "left"):
        orien_ln = "down"
    elif (orien_l == "down"):
        orien_ln = "right"
    elif (orien_l == "right"):
        orien_ln = "up"
    else:
        print("Orientation was not changed due to improper input")
    
    return orien_ln


def turn_right(orien_r: str) -> str:
    '''turn_right changes the orientation or the robot by turning right

    this function takes in an orientation as a string and outputs a new orientation based on the original

    Args:
        orien_r (str): the original robot orientation before the function was called

    Returns:
        str: the new robot orientation after turning right
    '''
    # Sart with the orienation not changing
    orien_rn = orien_r
    
    # determine the current orientation then turn
    if (orien_r == "up"):
        orien_rn = "right"
    elif (orien_r == "left"):
        orien_rn = "up"
    elif (orien_r == "down"):
        orien_rn = "left"
    elif (orien_r == "right"):
        orien_rn = "down"
    else:
        print("Orientation was not changed due to improper input")
        
    return orien_rn

def update_robot(action: str, orien_u: str, pos_u: List[int], obs_u: List[List[int]]):
    '''update_robot update the robot position and orientation based on user input

    _extended_summary_

    Args:
        action (str): the action the user entered: w: forward, s: backwards, a: left, d: right, q: quit
        orien_u (str): orientation of the robot (up, down, left, right)
        pos_u (List[int]): positon of the robot in x-y coordinates with the origin at the top left
        obs_u (List[List[int]]): a list of the x-y coordinates of the robot

    Returns:
        pos_result (List[int]): updated postion of the robot
        orien_result (str): update the orientation of the robot
    '''

    # using deep copy to ensure I have a result while not changing the original
    orien_result = deepcopy(orien_u)
    pos_result = deepcopy(pos_u)
    
    # move based on the action
    if (action == 'w'):
        pos_result = move_forward(orien_u, pos_u, obs_u)
    elif (action == 'a'):
        orien_result = turn_left(orien_u)
    elif (action == 's'):
        pos_result = move_backward(orien_u, pos_u, obs_u)
    elif (action == 'd'):
        orien_result = turn_right(orien_u)
    elif (action == 'q'):
        quit()
    else:
        print("Improper input, please enter w for forward, s for reverse, a for turning left, d for turning right, and q for quit")
            
    return pos_result, orien_result


