# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 7    -- #
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
# # --     SLIDE 9     -- #
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
# # --     SLIDE 13    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def greet(name):
#     return f"Hello, {name}!"

# my_variable = greet
# print(type(my_variable))  # <class 'function'>
# print(my_variable("Alice"))  # Hello, Alice!

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 14    -- #
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
# # --     SLIDE 15    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def make_multiplier(factor):
#     def multiplier(number):
#         return number * factor

#     return multiplier


# # Creating a doubler and tripler function
# doubler = make_multiplier(2)
# tripler = make_multiplier(3)

# print(doubler(5))  # 10
# print(tripler(5))  # 15

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 16    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def add(x, y):
#     return x + y


# def subtract(x, y):
#     return x - y


# operations = [add, subtract]
# print(operations[0](5, 3))  # 8 (addition)
# print(operations[1](5, 3))  # 2 (subtraction)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 20    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# # standard function
# def add(x, y):
#     return x + y


# print(add(1, 3))  # 4

# lambda expression
# add = lambda x, y: x + y
# print(add(1, 3))  # 4

# ------------------- #

# # standard function
# def double(x):
#     return x * 2

# print(double(2))  # 4

# lambda expression
# double = lambda x: x * 2
# print(double(2))  # 4

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 21    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# import dis

# # lambda expression
# dis.dis(lambda x: x * 2)

# print("--" * 20)


# # standard function
# def double(x):
#     return x * 2


# dis.dis(double)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 22    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# print((lambda x: x + 1)(2)) # 3
# (lambda x: assert x == 2)(2) # SyntaxError: invalid syntax
# print((lambda x: int: x + 1)(2) ) # SyntaxError: invalid syntax
# print((lambda x, y, z: x + y + z)(1, 2, 3))  # Positional arguments
# print((lambda x, y, z=3: x + y + z)(1, 2))  # Default arguments
# print((lambda x, y, z: x + y + z)(1, z=2, y=2))  # Keyword arguments
# print((lambda *args: sum(args))(1, 2, 3))  # lambda with *args
# print((lambda **kwargs: kwargs)(a=1, b=2, c=3))  # lambda with **kwargs

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 24    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # [1, 4, 9, 16, 25]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 25    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# numbers = [1, 2, 3, 4, 5]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # [2, 4]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 26    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# pairs = [(1, "b"), (3, "a"), (2, "c")]
# sorted_pairs = sorted(pairs, key=lambda x: x[1])
# print(sorted_pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 27    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y: x + y, numbers)  # ((((1+2)+3)+4)+5)
# print(total)  # 15

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 28    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# numbers = [1, 2, 3, 4, 5]
# squared = [x ** 2 for x in numbers]
# even_numbers = [x for x in numbers if x % 2 == 0]

# print('--' * 20)

# words = ["apple", "fig", "banana", "cherry"]
# sorted_words = sorted(words, key=lambda word: len(word))
# print(sorted_words)  # Output: ['fig', 'apple', 'banana', 'cherry']

# print('--' * 20)

# data = [("apple", 3), ("fig", 2), ("apple", 5), ("fig", 1)]
# sorted_data = sorted(data, key=lambda x: (x[0], -x[1]))
# print(sorted_data)  # [('apple', 5), ('apple', 3), ('fig', 2), ('fig', 1)]

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 30    -- #
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

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 33    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def power_factory(exponent):
#     def power(base):
#         return base**exponent

#     return power


# # Create square and cube functions
# square = power_factory(2)
# cube = power_factory(3)

# print(square(4))  # 16
# print(cube(4))  # 64

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 34    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def make_counter():
#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter


# counter_a = make_counter()
# counter_b = make_counter()

# print(counter_a())  # 1
# print(counter_a())  # 2
# print(counter_b())  # 1

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 35    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def secure_access(data):
#     def access(key):
#         if key == "secret_key":
#             return data
#         else:
#             return "Access Denied"

#     return access


# data_access = secure_access("Sensitive Data")
# print(data_access("wrong_key"))  # Access Denied
# print(data_access("secret_key"))  # Sensitive Data


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 36    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def setup_callback(prefix):
#     def callback(message):
#         print(f"{prefix}: {message}")

#     return callback


# success_callback = setup_callback("Success")
# failure_callback = setup_callback("Failure")

# # Simulate invoking callbacks
# success_callback("Operation completed")  # Success: Operation completed
# failure_callback("An error occurred")  # Failure: An error occurred

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 37    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# # standard function
# def function_example():
#     print("This is a function.")


# # assign the function to a variable
# f = function_example

# #lambda
# add = lambda x, y: x + y

# print(callable(function_example))  # True
# print(callable(f))  # True
# print(callable(add))  # True

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 39    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def decorate(original_function):
#     def wrap_decorate():
#         print("~*" * 10)
#         original_function()
#         print("~*" * 10)

#     return wrap_decorate


# def display_hello():
#     print("Hello")


# # Applying the decorator to display_hello()
# decorated_hello = decorate(display_hello)
# display_hello()  # calls display_hello()
# print()
# decorated_hello()  # calls wrap_decorate()

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 40    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def decorate(original_function):
#     def wrap_decorate():
#         print("~*" * 10)
#         original_function()
#         print("~*" * 10)

#     return wrap_decorate


# @decorate
# def display_hello():
#     print("Hello")


# display_hello()  # calls wrap_decorate()

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 42    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def decorate(original_function):
#     def wrap_decorate():
#         print("~*" * 10)
#         original_function()
#         print("~*" * 10)

#     return wrap_decorate


# @decorate
# def greet(name=None):
#     if name is None:
#         print("Hello, Guest!")
#     else:
#         print(f"Hello, {name}!")


# greet(
#     "Alice"
# )  # TypeError: wrap_decorate() takes 0 positional arguments but 1 was given


# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 43    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def decorate(original_function):
#     def wrap_decorate(*args):
#         print("~*" * 10)
#         original_function(*args)
#         print("~*" * 10)

#     return wrap_decorate


# @decorate
# def greet(name=None):
#     if name is None:
#         print("Hello, Guest!")
#     else:
#         print(f"Hello, {name}!")


# greet("Alice")
# greet()

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 44    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def double_number(original_function):
#     def wrap_double_number(*args):
#         original_function(*args) * 2

#     return wrap_double_number


# @double_number
# def multiply(a, b):
#     print(f"Multiplying {a} and {b}")
#     return a * b


# @double_number
# def subtract(a, b):
#     print(f"Subtracting {b} from {a}")
#     return a - b


# print(multiply(2, 3))  # 12
# print(subtract(10, 3))  # 14

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 45    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# def create_stars(original_function):
#     def wrap_create_stars(*args, **kwargs):
#         print("*" * 30)
#         original_function(*args, **kwargs)
#         print("*" * 30)

#     return wrap_create_stars


# def create_dashes(original_function):
#     def wrap_create_dashes(*args, **kwargs):
#         print("-" * 30)
#         original_function(*args, **kwargs)
#         print("-" * 30)

#     return wrap_create_dashes


# @create_stars
# @create_dashes
# def display_hello():
#     print("Hello")


# display_hello()

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 46    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# import functools


# def decorate(original_function):
#     @functools.wraps(original_function)
#     def wrap_decorate(*args):
#         print("~*" * 10)
#         original_function(*args)
#         print("~*" * 10)

#     return wrap_decorate


# @decorate
# def greet():
#     """Print 'Hello'."""
#     print("Hello!")


# print(greet.__name__)  # greet
# print(greet.__doc__)  # Print 'Hello'.
# print(greet.__module__)  # __main__

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 47    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# import time
# import functools

# def timer(original_function):
#     @functools.wraps(original_function)
#     def wrap_timer(*args):
#         start_time = time.perf_counter()  # 1
#         value = original_function(*args)
#         end_time = time.perf_counter()  # 2
#         run_time = end_time - start_time  # 3
#         print(f"Finished {original_function.__name__!r} in {run_time:.4f} secs")
#         return value

#     return wrap_timer


# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])


# waste_some_time(1000)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 48    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# import time
# import functools


# def slow_down(original_function):
#     """Sleep 1 second before calling the function"""

#     @functools.wraps(original_function)
#     def wrap_slow_down(*args):
#         time.sleep(1)
#         return original_function(*args)

#     return wrap_slow_down


# @slow_down
# def countdown(from_number):
#     if from_number < 1:
#         print("Liftoff!")
#     else:
#         print(from_number)
#         countdown(from_number - 1)


# countdown(3)

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 49    -- #
# # %%%%%%%%%%%%%%%%%%%%% #

# -- exercise1 -- #
# @strong
# @emphasis
# def greet():
#     return "Hello"


# print(greet())  # <strong><em>Hello</em></strong>

# -- exercise2 -- #
# @count_calls
# def greet():
#   print 'Hello'

# greet() # call 1 of 'greet'
#         # Hello
# greet() # call 2 of 'greet'
#         # Hello

# # %%%%%%%%%%%%%%%%%%%%% #
# # --     SLIDE 50    -- #
# # %%%%%%%%%%%%%%%%%%%%% #
# from functools import partial


# def multiply(x, y):
#     return x * y

# # Create a new function that multiplies by 2
# double = partial(multiply, 2)

# # Now you can just pass one argument to double
# print(double(4))  # 8
# print(double(5))  # 10

# # # %%%%%%%%%%%%%%%%%%%%% #
# # # --     SLIDE 51    -- #
# # # %%%%%%%%%%%%%%%%%%%%% #
# from functools import partial


# def log(message, level):
#     levels = {"DEBUG": 10, "INFO": 20, "ERROR": 30}
#     print(f"[{level} - {levels[level]}]: {message}")


# # Creating partial functions for each log level
# debug_log = partial(log, level="DEBUG")
# info_log = partial(log, level="INFO")
# error_log = partial(log, level="ERROR")

# # Usage examples
# debug_log("This is a debug message.")
# info_log("This is an info message.")
# error_log("This is an error message.")
