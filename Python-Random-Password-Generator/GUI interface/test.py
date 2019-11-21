import tkinter as tk
def forget():
	try:
		p2.pack_forget()
	except:
		print('gone')
root = tk.Tk()
p1 = tk.Frame()
p2 = tk.Frame()
t1 = tk.Label(p1,text = "Hello")
t1.pack()
t2 = tk.Label(p2,text = 'Hi')
t2.pack()
b1 = tk.Button(p1,text = "forget",command = forget)
b1.pack()
p1.pack(side = 'left')
p2.pack(side = 'right')

root.mainloop()