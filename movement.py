# THIS FILE IS FOR ROBOT MOVEMENT
state = input()


def go():
    if state:
        print("go")
    else:
        print("wait")


def catch():
    if state:
        print("catch")
    else:
        print("wait")

def grab():
    if state:
        print("grab")
    else:
        print("wait")

def drop():
    if state:
        print("drop")
    else:
        print("wait")

def push():
    if state:
        print("push")
    else:
        print("wait")

def turn():
    if state:
        print("turn")
    else:
        print("wait")