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
lbGTitle = Label(generatorf,text = "Random Password Generator")
EtGPassword = Entry(generatorf,text = "Pleas Enter Password")
btnGGo = Button(generatorf,text = "Go !")
lbGTitle.grid(row = 0,column = 0)
EtGPassword.grid(row = 1, column = 0)
btnGGo.grid(row = 1, column = 1)
for x in range(0,6):
	cb[x].grid(row = x+2, column = 0)


#Vault Frame Create and Configure
lbVPassword = Label(vaultf,text = "Password")
EtVPassword = Entry(vaultf,text = "Password ... ")
lbVUsername =Label(vaultf,text = "Username")
EtVUsername = Entry(vaultf,text = "Username ... ")
lbVMemo = Label(vaultf,text = "Memo")
EtVMemo = Entry(vaultf,text = "Memo ...")
btnVSave = Button(vaultf,text = "Save !")
btnVFill = Button(vaultf,text = "Fill from Generator")
lbVPassword.grid(row = 1, column = 0)
EtVPassword.grid(row = 1, column = 1)
lbVUsername.grid(row =0 , column =0)
EtVUsername.grid(row = 0, column = 1)
lbVMemo.grid(row = 2, column = 0)
EtVMemo.grid(row = 2, column =1 )
btnVSave.grid(row = 3, column = 1,columnspan = 2)
btnVFill.grid(row = 1,column = 2)

#Password Manager Create and Configure

lbMSearch = Label(managerf,text = "Search in Vault")
lbMUsername=Label(managerf,text = "Username")
entMUsername =  Entry(managerf,text = "Password...")
lbMMemo=Label(managerf,text = "Memo")
entMMemo = Entry(managerf,text = "Memo ...")
btnMSearch = Button(managerf,text = "Search ! ")
lbMResult=Label(managerf,text = "Passwords information will display here ...")
lbMSearch.grid(row = 0, column = 0,columnspan = 2)
lbMUsername.grid(row = 1, column =0 )
lbMMemo.grid(row = 2, column = 0)
btnMSearch.grid(row =3 , column = 0,columnspan = 2)
lbMResult.grid(row = 1, column = 3,rowspan = 3)
entMUsername.grid(row = 1, column = 1)
entMMemo.grid(row =2 , column = 1)
#Frame Pack
generatorf.grid(row =0 , column = 0 )
vaultf.grid(row =0 , column = 1)
managerf.grid(row = 1, column =1 )
root.mainloop()
