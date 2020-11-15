import csv
User_Data = open('Users/john/john_User.csv', 'w')
fieldnames = ['Username', 'Memo','Password']
User_Data_Writer = csv.DictWriter(User_Data, fieldnames=fieldnames)
User_Data_Writer.writeheader()