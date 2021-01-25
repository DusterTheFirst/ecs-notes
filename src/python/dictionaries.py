# Dictionaries hold a key and a value
# A classic dictionary dictionary would look like such
d = {"hello": "a greeting", "goodbye": "a farewell message"}

{True: "hi", False: "bye"}

{1: False, 2: True, 3: False}

{"a": [1, 2, 3], "b": [], "c": [7]}

# The key is the item on the left, the value is the one on the right
# To get a value, you can index the map like a list
d["hello"]  # would return "a greeting"

d["aloha"]  # ERROR, the key does not exist

# You can not have duplicate keys
d1 = {"a": 7, "b": 10, "a": 4}  # This works, but will give a warning

d1["a"]  # returns 4, totally ignores the first "a"

d2 = {10: 17, 3: False, 40: []}  # They dont need to be the same value either

d2[10]  # returns 17
d2[3]  # returns false
d2[40]  # returns []

# You can check if a key is in a dictionary using the in operator
"a greeting" in d  # False
"hello" in d  # True

# You can also mutate or modify the dictionary
d["hello"] = "cringe :D"
d["hello"]  # returns "cringe :D"

# You can also add new values
d["aloha"]  # ERROR
d["aloha"] = "Hawaiian for 'hello'"
d["aloha"]  # returns "Hawaiian for 'hello'"

# To get and remove an item from the dictionary, you can
d.pop("aloha")  # returns "Hawaiian for 'hello'"
d["aloha"]  # ERROR

# you can also clear dictionaries
d.clear()

# We can also do things over all items in a dictionary
for key in d:
    print(key, ":", d[key]) # Will print key : value for all items