from tkinter import *
import random
from functools import partial
import random
root = Tk()
#Variable Declariation 
Letter = BooleanVar()
Numbers= BooleanVar()
Caps= BooleanVar()
Special_Characters= BooleanVar()
Easy_to_Read= BooleanVar()

Generate = StringVar()
Size = IntVar()
Username = StringVar()
Password = StringVar()
Memo = StringVar()
SUsername = StringVar()
SMemo = StringVar()
word = []
chars = []
generate = []
special = ['!','@','#','$','%','&_','-','?']
ascii_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ascii_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Button Functions
def removeList(b):
	for i in b:
		chars.remove(i)
def appendLU():
	global chars
	if(Letter.get() == True):
		chars.extend(ascii_lowercase)
	else:
		removeList(ascii_lowercase)

def appendLL():
	global chars
	if(Caps.get() == True):
		chars.extend(ascii_uppercase)
	else:
		removeList(ascii_uppercase)

def appendN():
	global chars
	if(Numbers.get() == True):
		chars.extend(digits)
	else:
		removeList(digits)
def appendS():
	global chars
	if(Special_Characters.get() == True):
		chars.extend(special)
	else:
		removeList(special)
def Easy():
	global chars
	global word
	if(Easy_to_Read.get()==True):
		word = []
		for i in range(0,26):
			word.append(random.choice(open('English_noun.txt').readlines()).strip('\n'))
		print(word)
		chars.extend(word)
	else:
		removeList(word)
def Refresh():
	global chars
	global word
	if(Easy_to_Read.get()==True):
		word = []
		for i in range(0,26):
			word.append(random.choice(open('English_noun.txt').readlines()).strip('\n'))
		print(word)
		chars.extend(word)
	else:
		return
def Create():
	global generate
	generate = []
	for i in range(0,Size.get()):
		generate.append(random.choice(chars))
	Generate.set(''.join(generate))
	
def Fill():
	Password.set(Generate.get())

#Frame Creation
generatorf = Frame(root)
vaultf = Frame(root)
managerf = Frame(root)




#Generator Frame Create and Configure
cb = []
EtGSize = Entry(generatorf,text="Size",textvariable = Size)
cb.append(Checkbutton(generatorf,text="Letters", variable=Letter,onvalue = True, offvalue = False, height = 2,width = 15,command = appendLU))
cb.append(Checkbutton(generatorf,text="Numbers", variable=Numbers,onvalue = True, offvalue = False, height = 2,width = 15,command = appendN))
cb.append(Checkbutton(generatorf,text="Caps", variable=Caps,onvalue = True, offvalue = False, height = 2,width = 15,command = appendLL))
cb.append(Checkbutton(generatorf,text="Special Characters", variable=Special_Characters,onvalue = True, offvalue = False, height = 2,width = 15,command = appendS))
cb.append(Checkbutton(generatorf,text="Easy to Read", variable=Easy_to_Read,onvalue = True, offvalue = False, height = 2,width = 15,command = Easy))
lbGSize = Label(generatorf,text = "Size")
lbGTitle = Label(generatorf,text = "Random Password Generator")
EtGPassword = Entry(generatorf,text = "Pleas Enter Password",textvariable = Generate)
btnGGo = Button(generatorf,text = "Go !",command = Create )
btnGRefresh = Button(generatorf,text = "Refresh",command = Refresh )
lbGSize.grid(row =2,column = 1)
EtGSize.grid(row = 2,column = 0)
lbGTitle.grid(row = 0,column = 0)
EtGPassword.grid(row = 1, column = 0)
btnGGo.grid(row = 1, column = 1)
btnGRefresh.grid(row = 7,column = 1)
for x in range(0,5):
	cb[x].grid(row = x+3, column = 0)


#Vault Frame Create and Configure
LbVPassword = Label(vaultf,text = "Password")
EtVPassword = Entry(vaultf,text = "Password ... ",textvariable = Password)
LbVUsername =Label(vaultf,text = "Username")
EtVUsername = Entry(vaultf,text = "Username ... ",textvariable = Username)
LbVMemo = Label(vaultf,text = "Memo")
EtVMemo = Entry(vaultf,text = "Memo ...",textvariable = Memo)
BtnVSave = Button(vaultf,text = "Save !")
BtnVFill = Button(vaultf,text = "Fill from Generator",command = Fill)
LbVPassword.grid(row = 1, column = 0)
EtVPassword.grid(row = 1, column = 1)
LbVUsername.grid(row =0 , column =0)
EtVUsername.grid(row = 0, column = 1)
LbVMemo.grid(row = 2, column = 0)
EtVMemo.grid(row = 2, column =1 )
BtnVSave.grid(row = 3, column = 1,columnspan = 2)
BtnVFill.grid(row = 1,column = 2)

#Password Manager Create and Configure

LbMSearch = Label(managerf,text = "Search in Vault")
LbMUsername=Label(managerf,text = "Username")
EntMUsername =  Entry(managerf,text = "Username...",textvariable = SUsername)
LbMMemo=Label(managerf,text = "Memo")
EntMMemo = Entry(managerf,text = "Memo ...",textvariable = SMemo)
BtnMSearch = Button(managerf,text = "Search ! ")
LbMResult=Label(managerf,text = "Passwords information will display here ...")
LbMSearch.grid(row = 0, column = 0,columnspan = 2)
LbMUsername.grid(row = 1, column =0 )
LbMMemo.grid(row = 2, column = 0)
BtnMSearch.grid(row =3 , column = 0,columnspan = 2)
LbMResult.grid(row = 1, column = 3,rowspan = 3)
EntMUsername.grid(row = 1, column = 1)
EntMMemo.grid(row =2 , column = 1)
#Frame Pack
generatorf.grid(row =0 , column = 0 )
vaultf.grid(row =0 , column = 1)
managerf.grid(row = 1, column =1 )
root.mainloop()
