import socket

p=0
x=0
y=0
xString=''
yString=''
fire=''
answer=200
file=''
eboard=[]
hit=1
sink=''

def playerInput():
    global p
    global x
    global y
    global xString
    global yString
    player = input("Enter player (1 or 2): ")
    p=int(player)
    xString = input("Enter x coordinate: ")
    x=int(xString)
    yString = input("Enter y coordinate: ")
    y= int(yString)

def fireUpon():
    global fire
    fire = "x=%s y=%s" % (xString,yString)

def playerSelect(p):
    global file
    if p==1:
        file="eboard.txt"
    else:
        file="eboard2.txt"

def readFile(file):
    global eboard
    with open(file) as my_file:
        eboard = my_file.readlines()




def errorHandler(answer):
    global x
    global y
    if answer ==404:
        print("out of bounds.")
        xString = input("Enter x coordinate: ")
        x=int(xString)
        yString = input("Enter y coordinate: ")
        y=int(yString)

    if answer==410:
        print("spot already fired upon")
        xString = input("Enter x coordinate: ")
        x=int(xString)
        yString = input("Enter y coordinate: ")
        y = int(yString)

    if answer==400:
        print("bad request")
        xString = input("Enter x coordinate: ")
        x=int(xString)
        yString = input("Enter y coordinate: ")
        y = int(yString)

def responseHandler():
    if hit==1:
        row = list(eboard[y])
        row[x] = "X"
        eboard[y] = ''.join(row)
        f = open(file, 'w')
        f.truncate()
        for e in eboard:
            f.write(e)
    else:
        row = list(eboard[y])
        row[x] = "~"
        eboard[y] = ''.join(row)
        f= open(file, 'w')
        f.truncate()
        for e in eboard:
            f.write(e)

if __name__ == "__main__":
    playerInput()
    print(x,y)
    playerSelect(p)
    readFile(file)
    fireUpon()
    print(fire)
    while answer>=400:
        errorHandler(answer)
        fireUpon()
    responseHandler()