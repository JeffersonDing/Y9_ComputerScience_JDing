import csv
from pynput.keyboard import Key,Controller
import time
keyboard=Controller()
csvfile = open('User_Data.csv', 'r+')
fieldnames = ['Username', 'Memo','Password']
reader = csv.DictReader(csvfile)
str = "Hello this is a test"
time.sleep(3)
for row in reader:
	for a in row['Username']:
		keyboard.press(a)
		keyboard.release(a)
	keyboard.press('\n')
	keyboard.release('\n')