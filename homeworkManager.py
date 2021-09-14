#!/usr/bin/python3.9

import os
import time

job = "string"

run = True
assignments = []

class Homework:
    def __init__(self, teacher, due_date, name):
        self.name = name
        self.teacher = teacher
        self.due_date = due_date
        print("homework made")
    def __repr__(self):
        return "project name {}; teacher: {}; due: {}".format(self.name, self.teacher, self.due_date)

def setup():
    global run
    print("input 'make' if you want to make a new homework entry")
    job = input("what do you want to do? ")
    if job == "make":
        name = input("what is the homework name? ")
        teacher = input("who is the teacher? ")
        due_date = input("when us it due? ")
        assignments.append(Homework(teacher, due_date, name))
        print(assignments)
        if input("Anything else? ") == "no":
            run = False
        else:
            return

while run:
    setup()
    time.sleep(0.5)
