import csv
from pynput.keyboard import Key,Controller
import time
csvfile = open('User_Data.csv', 'r+')
a = csvfile.readlines(1)
print(a)
if(a==['Username,Memo,Password\n']):
	print('Obay')