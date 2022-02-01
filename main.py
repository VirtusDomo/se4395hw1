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

def numvalidate(info):
    print("Phone", info + " is invalid")
    print("Enter Phone Number in form 123-456-7890")
    num = input("Enter phone number: ")
    numcheck = re.search("[0-9]{3}-[0-9]{3}-[0-9]{4}", num)
    if numcheck:
        return num
    else:
        numvalidate(num)

def idvalidate(info):
    print("ID invalid: " + info)
    print("ID is two letters followed by 4 digits")
    ids = input("Please enter a valid id: ")
    idcheck = re.search("[A-Z][A-Z][0-9][0-9][0-9][0-9]", ids)
    if idcheck:
        return ids
    else:
        idvalidate(ids)


def processing(list):
    list.pop(0)
    people = {}
    #print(list)
    for i in range(len(list)):
        info = list[i].split(",")
        print(info)
        info[0] = info[0].capitalize()
        info[1] = info[1].capitalize()
        if info[2] != '':
            info[2] = info[2].capitalize()
        else:
            info[2] = "X"

        idcheck = re.search("[A-Z][A-Z][0-9][0-9][0-9][0-9]",info[3])
        if idcheck:
            continue
        else:
            temp = idvalidate(info[3])
            info[3] = temp

        numcheck = re.search("[0-9]{3}-[0-9]{3}-[0-9]{4}",info[4])
        if numcheck:
            continue
        else:
            temp2 = numvalidate(info[4])
            info[4] = temp2

        personMaker(info, people)

        p1 = Person(info[0], info[1], info[2], info[3], info[4])
        key = info[3]
        print(i)
        #people[i] = {key: p1}
        people[key] = p1.display()
        print(len(people))
    return people

def personMaker(info, people):
    p1 = Person(info[0], info[1], info[2], info[3], info[4])
    key = info[3]
    # people[i] = {key: p1}
    people[key] = p1.display()
    print(len(people))
return people

def main():
    if len(sys.argv) > 1:
        rp = sys.argv[1]
        listed = reader(rp)
        people = processing(listed)
        print(people)
    else:
        print('Error, insufficient path please retry.')

if __name__ == '__main__':
    main()
