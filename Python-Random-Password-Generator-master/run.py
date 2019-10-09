#!/usr/bin/env python
# -*- conding:utf-8 -*-

import os
import string
import random


def random_password_generator(size):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(0, size))
   

def random_password_generator_ico():
    random_password_generator_ico = """
    #############################################################
    #                  Random Password Generetor                #
    #                                                           #
    #             DEVELOPER :Jeofo                              #
    #          Mail Address : jefferson.ding@ucc.on.ca          #
    #               Teacher : Mr. Miskew                        #
    #                                                           #
    #############################################################
    """
    print(random_password_generator_ico)
    

def random_password_generator_register():
    print("Undv")


def random_password_generator_logon():
    name = input("Please Enter Your Username\n")
    if(name=="admin"):
        if(input("Please Enter Your Password\n")=="admin"):
            print("Welcom\t"+name+"\n\n")
            return True
    else:
        print("Username Not Found!!")

#Running
random_password_generator_ico()
sel = int(input("Please log on or Create a new account.\n1.logon\n2.Create new account\n"))
if(sel == 1):
    if(random_password_generator_logon()):
        opt = int(input("Please select the function\n1.Create new password\n2.Open password safe\n "))
        size = int(input("Please Enter Length of Password\n"))
        if(size<30):
            print("Password : " + random_password_generator(size))
        else:
            print("Password too long, are you sure about that ??")
        
elif(sel == 2):
    random_password_generator_register()
else:
    print("Please select a valid number")




