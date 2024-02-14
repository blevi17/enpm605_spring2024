# ========================#
# --- Dictionary Type --- #
# ========================#

# # ----Slide 30 ---- #
# fruit_genus = {
#     "watermelon": "citrullus",
#     "orange": "citrus",
#     "plum": "prunus",
#     "lemon": "citrus",
# }
# print(fruit_genus)

# # ----Slide 32 ---- #
# from pprint import pprint

# fruit_genus = {
#     "malus": {
#         "scientific": {
#             "malus angustifolia": {
#                 "common_name": "southern crabapple",
#                 "distribution": "southern united states",
#             },
#             "malus brevipes": {
#                 "common_name": "broadleaf crabapple",
#                 "distribution": "eastern united states",
#             },
#         }
#     }
# }

# pprint(fruit_genus, indent=2, width=40)

# # ----Slide 34 ---- #
# from pprint import pprint

# d = {
#     "TurtleBot3": "mobile",
#     "UR10": "industrial",
#     "Gapter": "aerial",
#     "TurtleBot3": "aerial",
#     "greeting": "hello",
#     1: "integer",
#     2.5: "float",
#     int: "type",
#     True: True,
#     (1, 2, 3): (1, 2, 3),
#     [1, 2, 3]: "hello",  # TypeError: unhashable type: 'list'
# }

# pprint(d)

# # ----Slide 36 ---- #
# d = dict()  # {}
# print(d)
# d = dict(a=1, b="hello")  # {'a': 1, 'b': 'hello'}
# print(d)
# print("-" * 10)

# d = dict({"a": 4, "b": 5})  # {'a': 4, 'b': 5}
# print(d)
# d = dict({"a": 4, "b": 5}, c=3, d=4)  # {'a': 4, 'b': 5, 'c': 3, 'd': 4}
# print(d)
# print("-" * 10)

# d = dict([["x", 5], ("y", -5)])  # {'x': 5, 'y': -5}
# print(d)
# d = dict([("x", 5), ("y", -5)])  # {'x': 5, 'y': -5}
# print(d)
# d = dict([("x", 5), ("y", -5)], z=8)  # {'x': 5, 'y': -5, 'z': 8}
# print(d)

# # ----Slide 37 ---- #
# d = {x: x**2 for x in [1, 2, 3]}  # {1: 1, 2: 4, 3: 9}
# print(d)
# d = {x.upper(): x * 2 for x in "oops"}  # {'O': 'oo', 'P': 'pp', 'S': 'ss'}
# print(d)

# # ----Slide 38 ---- #
# fruit_genus = {}

# fruit_genus["watermelon"] = "citrus"
# fruit_genus["orange"] = "citrus"
# fruit_genus["watermelon"] = "citrullus"
# print(fruit_genus)
# print("-" * 10)

# fruit_genus_1 = {"watermelon": "citrullus"}
# fruit_genus_2 = {"lemon": "citrus"}  # dictionary
# fruit_genus_1.update(fruit_genus_2)
# print(fruit_genus_1)  # {'lemon': 'citrus', 'watermelon': 'citrullus'}


# # ----Slide 39 ---- #
# fruit_genus = {
#     "watermelon": "citrullus",
#     "orange": "citrus",
#     "plum": "prunus",
#     "lemon": "citrus",
# }

# print(fruit_genus["orange"])
# print(fruit_genus["apple"])  # KeyError: 'apple'
# print('-' * 10)

# print(fruit_genus.get("orange"))  # citrus
# print(fruit_genus.get("apple"))  # None
# print(fruit_genus.get("apple", "apple is not a key"))  # apple is not a key

# # ----Slide 40 ---- #
# fruit_genus = {
#     "watermelon": "citrullus",
#     "orange": "citrus",
#     "plum": "prunus",
#     "lemon": "citrus",
# }


# def print_not_found(key):
#     print(f"{key} is not found")


# fruit_genus.get("apple", print_not_found("apple"))  # apple is not found

# # ----Slide 42 ---- #
# fruit_genus = {
#     "orange": "citrus",
#     "plum": "prunus",
# }

# fruit_keys = fruit_genus.keys()
# print(fruit_keys)  # dict_keys(['orange', 'plum'])
# fruit_genus["lemon"] = "citrus"
# print(fruit_keys)  # dict_keys(['orange', 'plum', 'lemon'])

# # ----Slide 43 ---- #
# fruit_genus = {
#     "orange": "citrus",
#     "plum": "prunus",
# }

# # iterate directly over the keys
# for key in fruit_genus:
#     print(key, end=" ")  # orange plum

# print()

# # view object
# keys = fruit_genus.keys()

# for key in keys:
#     print(key, end=" ")  # orange plum
# print()

# # ----Slide 44 ---- #
# fruit_genus = {
#     "orange": "citrus",
#     "plum": "prunus",
# }

# # iterate directly over the keys
# for key in fruit_genus:
#     print(fruit_genus[key], end=" ")  # citrus prunus

# print()

# # view object
# values = fruit_genus.values()

# for value in values:
#     print(value, end=" ")  # citrus prunus

# # ----Slide 45 ---- #
# fruit_genus = {
#     "orange": "citrus",
#     "plum": "prunus",
# }

# # iterate directly over the keys
# for key in fruit_genus:
#     print(key, fruit_genus[key], end=" ")  # orange citrus plum prunus

# print()

# # view object
# items = fruit_genus.items()

# for key, value in items:
#     print(key, value, end=" ")  # orange citrus plum prunus

# # ----Slide 46 ---- #
# fruit_genus = {
#     "orange": "citrus",
#     "plum": "prunus",
# }

# print(fruit_genus.pop("orange"))  # citrus
# print(fruit_genus)  # {'plum': 'prunus'}
# print(fruit_genus.pop("apple", "apple not found"))  # apple not found
# print(fruit_genus.pop("apple"))  # KeyError: 'apple'

# # ----Slide 47 ---- #
# fruit_genus = {
#     "plum": "prunus",
#     "orange": "citrus",
# }

# print(fruit_genus.popitem())  # ('orange', 'citrus')
# print(fruit_genus)  # {'plum': 'prunus'}
# fruit_genus["apple"] = "malus"
# print(fruit_genus)  # {'plum': 'prunus', 'apple': 'malus'}
# print(fruit_genus.popitem())  # ('apple', 'malus')
# print(fruit_genus)  # {'plum': 'prunus'}

# # ----Slide 48 - Exercise ---- #
fruit_genus = {
    "plum": "prunus",
    "orange": "citrus",
    "apple": "citrus",
    "plantain": "musa",
}

# In one line, update the value 'apple' to 'malus'
fruit_genus["apple"] = 'malus'
#fruit_genus.update({"apple":'malus'})

# In one line, change the key 'orange' to 'lemon'
fruit_genus['lemon'] = fruit_genus.pop("orange")
print(fruit_genus)

# Create a new dictionary (name it d) with items from fruit_genus. The keys in d must contain the substring 'pl'.
d = { key:value for key, value in fruit_genus.items() if "pl" in key}
print(d)