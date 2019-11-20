import csv
import fnmatch
csvfile = open('User_Data.csv', 'r+')
fieldnames = ['Username', 'Memo','Password']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
reader = csv.reader(csvfile)
for row in reader:
	print(row)