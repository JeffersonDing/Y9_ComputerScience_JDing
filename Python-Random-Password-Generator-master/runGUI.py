from tkinter import *
root = Tk()


#Frame Creation
generatorf = Frame(root)
vaultf = Frame(root)
managerf = Frame(root)


#Variable Declariation 
Letter = BooleanVar()
Numbers= BooleanVar()
Caps= BooleanVar()
Special_Characters= BooleanVar()
Easy_to_Read= BooleanVar()
Easy_to_Memorize= BooleanVar()


#Generator Frame Create and Configure
cb = []
cb.append(Checkbutton(generatorf,text="Letters", variable=Letter,onvalue = True, offvalue = False, height = 2,width = 15))
cb.append(Checkbutton(generatorf,text="Numbers", variable=Numbers,onvalue = True, offvalue = False, height = 2,width = 15))
cb.append(Checkbutton(generatorf,text="Caps", variable=Caps,onvalue = True, offvalue = False, height = 2,width = 15))
cb.append(Checkbutton(generatorf,text="Special Characters", variable=Special_Characters,onvalue = True, offvalue = False, height = 2,width = 15))
cb.append(Checkbutton(generatorf,text="Easy to Read", variable=Easy_to_Read,onvalue = True, offvalue = False, height = 2,width = 15))
cb.append(Checkbutton(generatorf,text="Easy to Memorize", variable=Easy_to_Memorize,onvalue = True, offvalue = False, height = 2,width = 15))
lbTitle = Label(generatorf,text = "Random Password Generator")
lbPassword = Entry(generatorf,text = "Pleas Enter Password")
btnGo = Button(generatorf,text = "Go !")
lbTitle.grid(row = 0,column = 0)
lbPassword.grid(row = 1, column = 0)
btnGo.grid(row = 1, column = 1)
for x in range(0,6):
	cb[x].grid(row = x+2, column = 0)


#Vault Frame Create and Configure


#Password Manager Create and Configure


#Frame Pack
generatorf.pack()
root.mainloop()
