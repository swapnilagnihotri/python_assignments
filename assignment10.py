
def printnumtable(x):
    print("--in printnumtable fucntion")
    sum = 0
    table = []
    for i in range(10):
        sum = sum + int(x)
        #print(sum)
        table.append(sum)
        i = i+1
    print(table)

def printeventillnum(x):
    print("--in printeventillnum fucntion")
    i = 1
    while (i <= x):
        if(i % 2 == 0 ):
            print(i)
        i = i+1

def printoddtillnum(x):
    print("--in printoddtillnum fucntion")
    i = 0
    while (i <= x):
        if(i % 2 != 0 ):
            print(i)
        i = i+1
def printfactorial(x):
    print("--in factorial fucntion")
    i = 1
    fact = 1
    while (i <= x):
        fact = fact * i
        i = i + 1
    print(fact)

def printsumofnaturalnumbers(x):
    print("--in printsumofnaturalnumbers function")
    i = 1
    sum = 0
    while (i <= x):
        sum = sum + i
        i = i + 1
    print(sum)

def main():
    print("print all number till the given number")
    printnumtable(4)
    print("print all even number till the given number")
    printeventillnum(10)
    print("print all odd number till the given number")
    printoddtillnum(11)
    print("print factorial of a given number ")
    printfactorial(5)
    print("print sum of all natural number till the given number")
    printsumofnaturalnumbers(5)


if __name__ == "__main__":
    main()