import os

def printsel(select):
	os.system("clear")
	print("Selected:")
	for x in selection:
		print(option[x-1])

print("\nWelcome to Random Password Generator!")
print("please select the option / options you want!")
print("Eg. : For Letters and Numbers Enter '1' press enter then input '2' \n\n")
print("after you finish selecting enter'5'\n ")
option = ["1.Letters","2.Numbers","3.Signs","4.Caps","5.Done"]
selection = []
for x in option:
	print(x)
for x in range(4):
	a= int(input("please enter:"))
	selection.append(a)
	printsel(selection)
	if(a==5):
		break

	

