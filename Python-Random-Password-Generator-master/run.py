import os
import string
import random
import base64
#                                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                            MMMMMMMMMMMMMMMMMNmmmmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                           MMMMMMMMMMMMMNho/--......-/ohmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                           MMMMMMMMMMNh/.```````````````.:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                           MMMMMMMMMh:`````````````````````-yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                           MMMMMMMN+.``.ddy+:://///:-+ydm-```/mMMMMMMMMMMMmdhhhhdmMMMNNMMMMMMMMMMNmmNMMMMNmmNMMMMMMMMMMMMmmmNMMMMMMMMMMMMMMMMM
#                           MMMMMMN/````-MMMMNNMMMMMNNMMMM/````-mMMMMMMMMd/-......:MMy::sMMmddNMMMo--oMMMMo--oMMMMMMMMMMMM+--yMMMMMMMMMMMMMMMMM
#                           MMMMMMo`````+MMMMMMMMMMMMMMMMMs`````/MMMMMMMd-..+hmmmddMMhMMyMM+..sMMM+..+MMMM+..oMMMMMMMMMMMM/..sMNNMMMMMMMMMMMMMM
#                           MMMMMN.````:MMMMMMMMMMMMMMMMMMM+`````mMMMMMM+../MMNmmmmNMy::om+-..-/+M+../hhhh/..oMo//hMMy//sM/..:/:::oNMMMMMMMMMMM
#                           MMMMMm`````oMMMMMMMMMMMMMMMMMMMy`````yMMMMMM:..sMMo----+Ms../mo:..:osM+...----...oM:..sMMo..+M/../yy/../MMMMMMMMMMM
#                           MMMMMm`````:MMMMMMMMMMMMMMMMMMM+`````hMMMMMM/..+MMdh+../Ms../MM+..oMMM+..+mmmm/..oM:..sMMo..+M/..yMMd...MMMMMMMMMMM
#                           MMMMMM:`````sNMMMMMMMMMMMMMMMMh.````.NMMMMMMd-..odmmo../Ms../MM+..+NNM+..+MMMM+..oM:..oNN+..+M/..sNNy..-MMMMMMMMMMM
#                           MMMMMMd.``--.:ymNNMMMMMMMNNmy/.`````yMMMMMMMMd/-..--..-+Ms../MMh-..:/Mo..oMMMM+..oMs-..::--.+M/.--::..-hMMMMMMMMMMM
#                           MMMMMMMy.`:ys-`.-:mMMMMMN/-.``````.sMMMMMMMMMMMmdhyyhdmNMmddmMMMmhhhdMmddmMMMMmddmMMmhyyhmmdmMmdmmhyyhmMMMMMMMMMMMM
#                           MMMMMMMMd:`.shsooyMMMMMMMo```````-hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                           MMMMMMMMMNy:.:+ooyMMMMMMMs````.-sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                           MMMMMMMMMMMMdo:..+MMMMMMMs..-ohNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                            MMMMMMMMMMMMMMmdmMMMMMMMNdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#                                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM


n=7441826991206406709576923798652306546773056383923657355748125433921170166237822700978602733318243198872391448038717383645273135292865009135623454648457251152479774667822283716405812196213269778591708092613681639094858652600822484100505704226715130775144353675554189536174751655752733823725881192996003709612306625816000913962672752947794794592929812789552418862834752848089722689574309164356302742239632448304296692333917423975797637051507227100217475335583330661060121209180098107074150139550375959262626119833501770072868699207069770140058936323994415274097579352438105654231135473547937006233631692474761658579637
e=6553
d=4165515245497497300584183807943943295218002566188306909947218692449695127385981026581644258478760270633897731024876447918642127308748489777119919372888935941903832364042749377655504217260838325633203919381502251213175879404824793480948408836195803400462305704552535818508925541477342845326801803129763712323707922729320122183190848453201638965312192858220393090816213720436537019479473566613916791146451770874471143677665974186271603566727889259702727174612886772425044819676162383477897768349836907574509704980372425128806961289095835294370498521487628563707891665120639474055335033475762900708067357970775016255657
cipher=[]
def random_password_generator(size):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(0, size))
   

def random_password_generator_ico():
    random_password_generator_ico = """
    #############################################################
    #                  Random Password Generetor                #
    #                                                           #
    #             DEVELOPER :Jeofo                              #
    #          Mail Address : jefferson.ding@ucc.on.ca          #
    #               Teacher : Mr. Miskew                        #
    #                                                           #
    #############################################################
    """
    print(random_password_generator_ico)
    

def random_password_generator_register():
    print("Undv")


def random_password_generator_logon():
    name = input("Please Enter Your Username\n")
    if(name=="admin"):
        if(input("Please Enter Your Password\n")=="admin"):
            print("Welcom\t"+name+"\n\n")
            return True
    else:
        print("Username Not Found!!")
def random_password_generator_encryptout(password):
    
def random_password_generator_decryptvault(cipher):

   




    
random_password_generator_ico()
sel = int(input("Please log on or Create a new account.\n1.logon\n2.Create new account\n"))
if(sel == 1):
    if(random_password_generator_logon()):
        opt = int(input("Please select the function\n1.Create new password\n2.Open password safe\n "))
        size = int(input("Please Enter Length of Password\n"))
        if(size<50):
            pwd = random_password_generator(size)
            print("Password : " + pwd)
            print("encrypt_password"+str(random_password_generator_encryptout(pwd)))

        else:
            print("Password too long, are you sure about that ??")
        
elif(sel == 2):
    random_password_generator_register()
else:
    print("Please select a valid number")




