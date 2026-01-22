
def display():
    print("Jay Ganesh")

def Chkgreater(a,b):
    if (a > b ):
        print("The greater number is",a)
    else:
        print("The greater number is",b)
def mysquare(x):
    print("The square of the given number is:",x*x)

def mycube(x):
    print("The cube of the given number is:",x*x*x)

def chkdivisibility(x):
    if((x % 3 == 0) & (x % 5 == 0)):
        print("the number"+str(x)+" is divisible by 3 and 5")
    else:
        print("the number "+str(x)+" is not divisible by 3 and 5")

def main():
    display()
    Chkgreater(10,20)
    mysquare(5)
    mycube(3)
    chkdivisibility(16)


if __name__ == "__main__":
    main()
