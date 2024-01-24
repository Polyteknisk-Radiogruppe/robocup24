# main.py
from movement import *

print("File1 __name__ = %s" %__name__)

if __name__ == "__main__":
    print("file is being run directly")
else:
    print("file is being imported")

print("TEST MOVEMENT w. STRINGS: go, grab, drop, turn, catch, go")
go()
grab()
drop()
turn()
go()