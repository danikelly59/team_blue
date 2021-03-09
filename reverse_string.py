"""
CSE 5408
"""

def reverse_string(str):
    str_a = ""
    for i in str:
        str_a = i + str_a
    return str_a

print("What do you want reversed?")
str = input()
    
print("Original message: ", str)
print("Reversed message: ",reverse_string(str))