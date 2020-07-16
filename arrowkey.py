import os
from time import sleep
from getpass import getpass

while True : 
    os.system("clear")
    print("+========================!!========================+")
    print("Tools By MR.BR0K3NH34RT And u0_a117")
    print("+========================!!========================+")
    os.system("figlet Arrow Key")
    print("+========================!!========================+")
    print("""
    1).Start Activation Of Arrow Key
    2).About This Tools
    3).Quit
    """)
    print("+========================!!========================+")
    code = raw_input("Please Choose : ")
    if code == "1":
        print("[!]Warning[!]")
        print("[!]Install At Your On Risk[!]")
        os.mkdir('/data/data/com.termux/files/home/.termux')
        key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
        kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
        kontol.write(key)
        kontol.close()
        sleep(1)
        os.system('termux-reload-settings')
        print("Activation Of Arrow Key Successed!")
    elif code == "2":
        print("+========================!!========================+")
        print("About This Tools")
        print ("This Tools Created By MR.BR0K3NH34RT And U0_A117")
        print("+========================!!========================+")
        print("""
 This Tools Make More Easier For Programmer Or Hacker To Do Some pentesting Or Tools
 This Tools Will Add Arrow Key On Your Terminal
        """)
        print("Do You Still Want To Use This Tools?")
        aku = raw_input(" [ Y/N ] : ")
        if aku == "y":
            print("Restarting Tools")
            os.system("python2 arrowkey.py")
        if aku == "n":
            print("Bye Dude :)")
            print("Have A Nice Day :)")
            break
    elif code == "3":
        print("Bye Dude :)")
        print("Have A Nice Day :)")
        print("")
        break
    else:
        print("Error 404(Not Found)")
    
    