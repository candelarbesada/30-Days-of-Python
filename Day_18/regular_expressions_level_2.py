# Day 18 - Level 2

import re

def is_valid_variable(var):
    if re.match(r'^[a-zA-Z\_]+[a-zA-Z0-9\_]*$', var):
        return True
    else:
        return False
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True