# Importing requirements
import random
import os
from Utils import *


# extract passwords


# Main function
def main():
    # Setting up variables
    ip = "./Users-Pwds.txt"
    op = "./Users-Pwds-Chked.txt"

    # Displaying description
    input_file = open(ip, 'r')
    output_file = open(op, 'a')
    lines = input_file.readlines()
    usrpwds = extractor(lines)
    for a in usrpwds:
        upwds = [a, usrpwds[a]]
        strength = rank(usrpwds[a])
        upwds.append(strength + '\n')
        upstr = (', ').join(upwds)
        output_file.write(upstr)
    output_file.close()


# checking strength
def rank(password):  # Checks strength of passwords by converting each string to ASCII code and counting
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
