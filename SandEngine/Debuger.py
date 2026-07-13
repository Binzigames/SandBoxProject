# WELCOME TO MY SWEET CONSOLE-DEBUGER (a print functions is here!)
#importing for you honey ~
from SandEngine.Libs import *

def print_message(message, Type=0):
    if Type == 0:
        print("DEBUGGER MESSAGE / ENGINE" + c.Fore.GREEN)
        print(str(message) + c.Fore.WHITE)
        print("==================================" + c.Fore.WHITE)

    elif Type == 1:
        print("DEBUGGER MESSAGE / ERROR" + c.Fore.RED)
        print(str(message) + c.Fore.WHITE)
        print("==================================" + c.Fore.WHITE)

    elif Type == 2:
        print("DEBUGGER MESSAGE / GAME" + c.Fore.YELLOW)
        print(str(message) + c.Fore.WHITE)
        print("==================================" + c.Fore.WHITE)

    else:
        print("Unknown debug type")


def print_init():
    print("==================================" + c.Fore.GREEN)
    print("SAND ENGINE LOADED / WELCOME" + c.Fore.WHITE)
    print("Nice to see you! your log is here:" )
    print("==================================" + c.Fore.GREEN)