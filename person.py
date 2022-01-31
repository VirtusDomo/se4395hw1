#Homework 1: Text Processing with Python
#Created by James Anyabine
#Completed by 1.30.2022

class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print("Employee ID: "+ self.id)
        print("\t\t"+ self.first, self.mi, self.last)
        print("\t\t"+ self.phone)


