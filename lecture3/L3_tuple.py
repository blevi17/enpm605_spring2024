# ==================#
# --- Tuple Type --- #
# ==================#
# testing the commit

# # ----Slide 25 ---- #
# a = (1, 2, 3)
# b = (1, "hello", 3.5)
# c = ("a", [1, 2, 3.5], (1, 2, 3))

# # ----Slide 27 ---- #
# fruits = ("apple", "kiwi", "orange")
# print(fruits)  # ('apple', 'kiwi', 'orange')
# print('-' * 10)

# fruits = 'apple', 'kiwi', 'orange'
# print(fruits)  # ('apple', 'kiwi', 'orange')
# print("-" * 10)

# # singleton
# fruits = 'apple'
# print(type(fruits))  # <class 'str'>
# print("-" * 10)

# fruits = 'apple',
# print(type(fruits))  # <class 'tuple'>


# # ----Slide 28 ---- #
# fruits = ("apple", "kiwi")
# fruit1, fruit2 = fruits
# print(fruit1, fruit2)  # apple kiwi

# fruits = ("apple", "kiwi", "orange")
# # fruit1, fruit2 = fruits  # ValueError: too many values to unpack (expected 2)
# fruit1, fruit2, fruit3, fruit4 = fruits  # ValueError: not enough values to unpack (expected 3, got 2)
# print('-' * 10)

# fruits = ("apple", "kiwi", "orange")
# fruit1, _, fruit3 = fruits
# print(fruit1, fruit3)  # apple orange
# print("-" * 10)

# fruits = ["apple", "kiwi", "orange"]
# fruit1, fruit2, fruit3 = fruits
# print(fruit1, fruit2, fruit3)  # apple kiwi orange
# print("-" * 10)

# # ----Slide 29 ---- #
# fruits = ("apple", "kiwi", "orange")
# fruits[0] = "cherry"  # TypeError: 'tuple' object does not support item assignment
# fruits[1:] = "cherry"  # TypeError: 'tuple' object does not support item assignment
# del fruits[0]  # TypeError: 'tuple' object doesn't support item deletion
# del fruits  # OK

# fruits = ("apple", ["kiwi", "orange"])
# fruits[1][0] = "cherry"
# print(fruits)  # ('apple', ['cherry', 'orange']
# fruits[1] = []  # TypeError: 'tuple' object does not support item assignment