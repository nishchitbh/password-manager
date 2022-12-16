# Importing requirements
import random
import os
from Utils import *


# extract passwords


# Main function
def main():
    # Setting up variables
    ip = "./Users-Pwds.txt"
    op = "Users-Pwds-Chked.txt"

    # Displaying description
    input_file = open("Users-Pwds.txt", 'r')
    lines = input_file.readlines()
    usrpwds = extractor(lines)
    for i in passwords:
        pass


# checking strength
def strength_check(password):  # Checks strength of passwords by converting each string to ASCII code and counting
    # types of characters
    length = len(password)
    a = list(map(ord, password))
    combinations = list(map(asc_to_txt, a))
    types = len(set(combinations))
    if length < 8 and types < 3:
        return ("POOR")
    elif length >= 8 and types == 3:
        return ("MODERATE")
    else:
        return ("STRONG")


## Test and debug
print(strength_check("Hello123$%^"))
