"""
This is the main file which contains the entry point of your program.
"""

from maze import print_maze

def main():
    print("Initial Maze:")
    print_maze()
    while True:
        action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")
        # TODO write the main function
        # Ctrl-c to stop the program
        print_maze()


# Run the main function
if __name__ == "__main__":
    main()
