#Homework 1: Text Processing with Python
#Created by James Anyabine
#Completed on 1.30.2022

import sys
import os
import pathlib
import person

def method1(filepath):

    print("\nUsing method 1")

    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    print(text_in)

def processing():






def main():
    if len(sys.argv) > 1:
        rp = sys.argv[1]
        method1(rp)
    else:
        print('Error, insufficient path please retry.')

if __name__ == '__main__':
    main()
