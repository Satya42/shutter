# importing the pyttsx library
import pyttsx3
import os
import subprocess

os.system("pip install pyttsx3")

os.system("cls")
# initialisation
engine = pyttsx3.init()
sound = engine.getProperty('voices')
engine.setProperty('voice', sound[1].id)

def shutdown():
    print("\n \033[01;36m Your Computer is shutdown\n")

def restart():
    print("\n \033[01;36m Your Computer is Restart\n")

def lock():
    print('\n \033[01;36m Your computer is lock\n')

def logout():
    print('\n \033[01;36m Your computer is logout\n')

print("\n \033[01;32m Choose Options Restart, Shutdown, Lock and Logout\n")

computer = ''

while computer != 'q':
    print("\t \033[01;35m Satya")
    print('\n \033[01;36m[1] Enter 1 to your computer is shutdown')
    print('\033[01;36m [2] Enter 2 to your computer is restart')
    print("\033[01;36m [3] Enter 3 to Lock Your computer")
    print('\033[01;36m [4] Enter 4 to Logout Your computer')
    print('\033[01;36m [q] Enter q to exit')

    computer = input('\033[01;36m Choose Options and Hit enter: ')
    if computer == '1':
        shutdown()
        os.system("shutdown /s /t 1")
    elif computer == '2':
        restart()
        os.system("shutdown /r /t 1")
    elif computer == '3':
        lock()
        cmd='rundll32.exe user32.dll, LockWorkStation'
        subprocess.call(cmd)
    elif computer == '4':
        logout()
        os.system('shutdown -l')
    elif computer == 'q':
        print("\n \033[01;36m Thanks")
        engine.say("thanks for quit")
    else:
        print("\n \033[01;31m Thanks! But Sorry Please try again another command\n")
print("\033[01;37m Created By Satya!")
engine.say("Thanks, for, using,")

engine.runAndWait()
