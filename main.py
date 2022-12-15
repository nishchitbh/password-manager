# Importing requirements
import random
import os


# extract passwords
def extractor(lines):  # Takes list of lines as input
    pw = []
    for i in lines:
        pwd = i.replace('\n', '').split(',')[-1].lstrip()
        pw.append(pwd)
    return pw


# Main function
def main():
    # Setting up variables
    ip = "./Users-Pwds.txt"
    op = "Users-Pwds-Chked.txt"

    # Displaying description
    input_file = open("Users-Pwds.txt", 'r')
    lines = input_file.readlines()
    passwords = extractor(lines)
    for i in passwords:
        pass


# checking strength
def strength_check(password):
    length = len(password)
    a = list(map(ord, password))
    combinations = list(map(asc_to_txt, a))
    types = len(set(combinations))
    if length < 8 and types < 3:
        return ("POOR")
    elif length >= 8 and types == 3:
        return("MODERATE")
    else:
        return("STRONG")


def asc_to_txt(asc):
    if asc >= 65 and asc <= 90:
        return 'U'
    elif asc >= 48 and asc <= 57:
        return 'N'
    elif asc >= 97 and asc <= 122:
        return 'L'
    else:
        return 'S'

## Test and debug
print(strength_check("Hello123$%^"))
