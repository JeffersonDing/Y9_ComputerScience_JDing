import os
print("\nWelcome to Random Password Generator!")
print("please select the option / options you want!")
print("Eg. : For Letters and Numbers Enter '1' press enter then input '2' \n\n")
print("after you finish selecting enter'5'\n ")

option = ["1.Letters","2.Numbers","3.Signs","4.Caps","5.Done"]
for x in option:
		print(x)

select = []
while( choise != 5):
	choise = int(input("Please enter:"))
	select.append(choise) 
	print(select)

		