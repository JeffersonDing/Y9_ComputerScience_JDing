from tkinter import *
 
def putX1():
	global bon
	if(bon==True):
	    intx1.set("X")
	    bon = not bon
	else:
		intx1.set("O")
		bon = not bon
def putX2():
	global bon
	if(bon==True):
	    intx2.set("X")
	    bon = not bon
	else:
		intx2.set("O")
		bon = not bon
def putX3():
	global bon
	if(bon==True):
	    intx3.set("X")
	    bon = not bon
	else:
		intx3.set("O")
		bon = not bon
def putX4():
	global bon
	if(bon==True):
	    intx4.set("X")
	    bon = not bon
	else:
		intx4.set("O")
		bon = not bon
def putX5():
	global bon
	if(bon==True):
	    intx5.set("X")
	    bon = not bon
	else:
		intx5.set("O")
		bon = not bon
def putX6():
	global bon
	if(bon==True):
	    intx6.set("X")
	    bon = not bon
	else:
		intx6.set("O")
		bon = not bon
def putX7():
	global bon
	if(bon==True):
	    intx7.set("X")
	    bon = not bon
	else:
		intx7.set("O")
		bon = not bon
def putX8():
	global bon
	if(bon==True):
	    intx8.set("X")
	    bon = not bon
	else:
		intx8.set("O")
		bon = not bon
def putX9():
	global bon
	if(bon==True):
	    intx9.set("X")
	    bon = not bon
	else:
		intx9.set("O")
		bon = not bon

root = Tk()
bon =True
intx1 = StringVar()
intx2 = StringVar()
intx3 = StringVar()
intx4 = StringVar()
intx5 = StringVar()
intx6 = StringVar()
intx7 = StringVar()
intx8 = StringVar()
intx9 = StringVar()
title = Label(text = "Tic Tac Toe Game")
title.grid(row = 0, column = 0,columnspan = 3)
button1 = Button(textvariable=intx1,command = putX1)
button2 = Button(textvariable=intx2,command = putX2)
button3 = Button(textvariable=intx3,command = putX3)
button4 = Button(textvariable=intx4,command = putX4)
button5 = Button(textvariable=intx5,command = putX5)
button6 = Button(textvariable=intx6,command = putX6)
button7 = Button(textvariable=intx7,command = putX7)
button8 = Button(textvariable=intx8,command = putX8)
button9 = Button(textvariable=intx9,command = putX9)
button1.grid(row =1 ,column =0)
button2.grid(row =1 ,column =1)
button3.grid(row =1 ,column =2)
button4.grid(row =2 ,column =0)
button5.grid(row =2 ,column =1)
button6.grid(row =2 ,column =2)
button7.grid(row =3 ,column =0)
button8.grid(row =3 ,column =1)
button9.grid(row =3 ,column =2)
root.mainloop()