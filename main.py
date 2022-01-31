#Homework 1: Text Processing with Python
#Created by James Anyabine
#Completed on 1.30.2022

import sys
import os
import re
from person import Person

def reader(filepath):

    print("\nUsing method 1")

    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        #text_in = f.read()
        lines = [line for line in f.readlines()]
    return lines

def processing(list):
    list.pop(0)
    people = { }
    for i in range(len(list)):
        info = list[i].split(",")
        info[0] = info[0].capitalize()
        info[1] = info[1].capitalize()
        if info[2]:
            info[2] = info[2].capitalize()
        else:
            info[2] = "X"

        idcheck = re.search("[A-Z][A-Z][0-9][0-9][0-9][0-9]",info[3])
        if idcheck:
            continue
        else:
            print("ID invalid: "+ info[3])
            print("ID is two letters followed by 4 digits")
            info[3] = input("Please enter a valid id: ")
        numcheck = re.search("[0-9]{3}-[0-9]{3}-[0-9]{4}",info[4])
        if numcheck:
            continue
        else:
            print("Phone",info[4]+" is invalid")
            print("Enter Phone Number in form 123-456-7890")
            info[4] = input("Enter phone number: ")

       # info[4] = re.sub("\D","-",info[4])
        #if info[4][3] != "-":
         #   info[4].insert(3, "-")
        #if info[4][7] != "-":
        #    info[4].insert(7, "-")
        p1 = Person(info[0], info[1], info[2], info[3], info[4])

        people = {info[3]: p1}
        #ppl = {}
        #for p in ppl:
         #   ppl[info[3]] = p
    return people

def main():
    if len(sys.argv) > 1:
        rp = sys.argv[1]
        listed = reader(rp)
        dict = processing(listed)

    else:
        print('Error, insufficient path please retry.')

if __name__ == '__main__':
    main()
