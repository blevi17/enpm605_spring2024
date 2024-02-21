# ------------------- #
# Functions: Part 1
# ------------------- #

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 9     -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def greet(name):
#     """
#     Function to greet a person by name.

#     Args:
#         name (str): Name of the person to greet.

#     Returns:
#         str: Greeting message.
#     """

#     return f"Hello, {name}!"


# print(greet.__doc__)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 11    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def add_numbers(a, b):
#     return a + b


# a = 5
# b = 3
# print(add_numbers(a, b))


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 15    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def add_numbers(a: str, b: int) -> list:
#     return a + b

# result = add_numbers(5, 3)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 16    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# from typing import List, Dict


# def process_items(items: List[int]) -> None:
#     for item in items:
#         print(item)


# def student_scores(scores: Dict[str, int]) -> None:
#     for student, score in scores.items():
#         print(f"{student}: {score}")

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 17    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# from typing import Optional, Union


# def greet(name: Optional[str] = None) -> str:
#     if name is None:
#         return "Hello, Guest!"
#     else:
#         return f"Hello, {name}!"


# def process_input(input_value: Union[int, str]) -> None:
#     if isinstance(input_value, int):
#         print(f"Integer: {input_value}")
#     else:
#         print(f"String: {input_value}")

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 19    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def display_info(name, age):
#     print(f"{name=}, {age=}")


# # Correct usage
# display_info("Alice", 30)  # name=Alice, age=30

# # Incorrect usage would result in a mismatch of values
# display_info(30, "Alice")  # name=30, age='Alice'

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 20    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def display_info(name, age=35):
#     print(f"{name=}, {age=}")


# # Calling function without age argument
# display_info("Bob")  # name=Bob, age=35
# display_info("Alice", 30)  # name=Alice, age=30

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 21    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def print_arguments(a=5, b):  # SyntaxError
#     print(a, b)

# def print_arguments(b, a=5):
#     print(a, b)


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 22    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def append_to_list(item, my_list=[]):
#     my_list.append(item)
#     return my_list


# print(append_to_list("a"))  # Expected ['a'], actual ['a']
# print(append_to_list("b"))  # Expected ['b'], actual ['a', 'b']

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 23    -- #
# # %%%%%%%%%%%%%%%%%%%%% #


# def append_to_list(item, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(item)
#     return my_list


# print(append_to_list("a"))  # Expected ['a'], actual ['a']
# print(append_to_list("b"))  # Expected ['b'], actual ['b']

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 24    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def create_user(name, age, isAdmin):
#     print(f"{name=}, {age=}, {isAdmin=}")


# # Using keyword arguments
# create_user(age=30, isAdmin=True, name="Alice")  # name='Alice', age=30, isAdmin=True

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 25    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def create_user(name, age, isAdmin=True):
#     print(f"{name=}, {age=}, {isAdmin=}")

# create_user("John Doe", isAdmin=False, age=30)
# # create_user(name="John Doe", 30, isAdmin=False) # SyntaxError

# # create_user(30, name="John Doe", isAdmin=False) # SyntaxError

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 27    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def print_all(*args):
#     print(type(args)) # <class 'tuple'>
#     for arg in args:
#         print(arg)


# print_all(1, "hello", True, 3.14)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 28    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def print_key_values(**kwargs):
#     print(type(kwargs))  # <class 'dict'>
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_key_values(name="John", age=30, country="USA")

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 29    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def print_everything(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_everything(1, "Apple", username="john_doe", age=25)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 31    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def unpack_args(x, y, z):
#     print(f"{x=}, {y=}, {z=}")


# # tuple
# args = 1, "a", 3
# unpack_args(*args)  # unpack_args(1, 'a', 3)

# # list
# args = [1, "a", 3]
# unpack_args(*args)  # unpack_args(1, 'a', 3)

# # set
# args = {1, "a", 3}
# unpack_args(*args)  # unpack_args(1, 3, 'a')

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 32    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def unpack_kwargs(a, b, c):
#     print(f"{a=}, {b=}, {c=}")

# kwargs = {"a": 1, "b": 2, "c": 3}
# unpack_kwargs(**kwargs)  # unpack_kwargs(a=1, b=2, c=3)


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 34    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def local_test(local_param):
#     local_var = "I am local var"
#     print(local_param)  # Accessible here
#     print(local_var)  # Accessible here

# local_test("I am local param")
# # print(local_var)  # NameError: name 'local_var' is not defined
# # print(local_param)  # NameError: name 'local_param' is not defined

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 35    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def outer_func():
#     enclosing_var = "I am enclosing"

#     def inner_func():
#         print(enclosing_var)  # Accessible here as an enclosing variable
#     # Call the inner function
#     inner_func()

# # Call the outer function
# outer_func()

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 36    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def outer_func():
#     enclosing_var = "outer function"

#     def inner_func():
#         # nonlocal enclosing_var
#         enclosing_var = "inner function"
#         print(enclosing_var)  # Accessible here as a local variable

#     inner_func()
#     print(enclosing_var)  # Accessible here as an enclosing variable


# outer_func()

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 37    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# global_var = "I am global"


# def my_func():
#     print(global_var)  # Accessible here


# my_func()

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 38    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# global_var = "I am global"


# def my_func():
#     # global global_var
#     global_var = "I am local"
#     print(global_var)  # "I am local"


# my_func()
# print(global_var)  # "I am global"

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 39    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# fruits = ["apple", "banana", "cherry"]


# def add_to_list(a):
#     fruits.append(a)


# add_to_list("orange")
# print(fruits)


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 40    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# print(dir(__builtins__))

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 41    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def outer_function():
#     a = 10
#     b = 10

#     def inner_function():
#         global b
#         # nonlocal b
#         b = 100
#         a = 100
#         print(f"inner: {a=} {b=}")

#     inner_function()

# outer_function()


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 43    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def update_number(x):
#     x = 10  # This creates a new object and binds 'x' to it locally


# num = 5
# update_number(num)
# print(num)  # Output: 5, because 'num' still references the original object

# ------------------- #

# def update_list(a_list):
#     a_list.append(4)  # Modifies the list object in place


# my_list = [1, 2, 3]
# update_list(my_list)
# print(my_list)  # Output: [1, 2, 3, 4], the original list is modified


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 44    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def edit_inputs(fruits, animals, age):
#     fruits.append("cherry")
#     fruits[0] = "mango"
#     fruits = ["quince", "pear"]
#     animals = ["elephant"]
#     age += 1


# fruits = ["apple", "banana"]
# animals = ["bear", "tiger"]
# age = 40

# print(fruits, animals, age)
# edit_inputs(fruits, animals, age)
# print(fruits, animals, age)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 47    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# # Define the number for which to calculate the factorial
# number = 5

# # Initialize the factorial result to 1 (the identity value for multiplication)
# factorial = 1

# # Use a for loop to multiply the result by each number from 1 to the specified number
# for i in range(1, number + 1):
#     factorial *= i

# # Print the result
# print(f"The factorial of {number} is {factorial}")


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 49    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# # Function to get dimensions of the rectangle
# def get_dimensions():
#     length = float(input("Enter the length: "))
#     width = float(input("Enter the width: "))
#     return length, width


# # Function to calculate the area of the rectangle
# def calculate_area(length, width):
#     return length * width


# # Function to display the area
# def display_area(area):
#     print(f"The area of the rectangle is: {area}")


# # Main function to orchestrate the procedural steps
# def main():
#     length, width = get_dimensions()
#     area = calculate_area(length, width)
#     display_area(area)


# # Entry point of the program
# if __name__ == "__main__":
#     main()


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 52    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def greet(name):
#     return f"Hello, {name}!"


# say_hello = greet
# print(say_hello("Alice"))  # Hello, Alice!

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 53    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def shout(text):
#     return text.upper() + "!"


# def whisper(text):
#     return text.lower() + "..."


# def greet(style, name):
#     message = f"Hello, {name}"
#     return style(message)


# # Passing the 'shout' and 'whisper' functions as arguments
# print(greet(shout, "Bob"))  # HELLO, BOB!
# print(greet(whisper, "Eve"))  # hello, eve...

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 54    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def make_multiplier(factor):
#     def multiplier(number):
#         return number * factor

#     return multiplier


# # Creating a doubler and tripler function
# doubler = make_multiplier(2)
# tripler = make_multiplier(3)

# print(doubler(5))  # Output: 10
# print(tripler(5))  # Output: 15

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 55    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# def add(x, y):
#     return x + y


# def subtract(x, y):
#     return x - y


# operations = [add, subtract]
# print(operations[0](5, 3))  # Output: 8 (addition)
# print(operations[1](5, 3))  # Output: 2 (subtraction)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 58    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# add = lambda x, y: x + y
# print(add(1, 3))  # 4

# double = lambda x: x * 2
# print(double(2))  # 4

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 59    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# import dis

# # lambda expression
# dis.dis(lambda x: x * 2)

# print("-------------------")

# # standard function
# def double(x):
#     return x * 2


# dis.dis(double)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 60    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# print((lambda x: x + 1)(2))  # 3
# print((lambda x: assert x == 2)(2))  # SyntaxError
# (lambda x: int: x + 1)(2)
# print((lambda x: 
#     x + 1)(2))
# print((lambda x, y, z: x + y + z)(1, 2, 3))  # Positional arguments
# print((lambda x, y, z=3: x + y + z)(1, 2))  # Default arguments
# print((lambda x, y, z: x + y + z)(1, z=2, y=2))  # Keyword arguments
# print((lambda *args: sum(args))(1, 2, 3))  # lambda with *args
# print((lambda **kwargs: kwargs)(a=1, b=2, c=3))  # lambda with **kwargs

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 62    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # [1, 4, 9, 16, 25]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 63    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# numbers = [1, 2, 3, 4, 5]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # [2, 4]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 64    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# pairs = [(1, "b"), (3, "a"), (2, "c")]
# sorted_pairs = sorted(pairs, key=lambda x: x[1])
# print(sorted_pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 65    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y: x + y, numbers)  # ((((1+2)+3)+4)+5)
# print(total)  # 15

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 68    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# import tkinter as tk


# # Function to handle button click
# def button_click():
#     print("Button clicked!")


# # Create a Tkinter window
# window = tk.Tk()
# window.title("Button Click Example")

# # Create a button widget with a lambda expression as its command
# button = tk.Button(window, text="Click Me", command=lambda: button_click())
# button.pack()

# # Run the Tkinter event loop
# window.mainloop()