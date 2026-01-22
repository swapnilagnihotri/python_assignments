
def checkVowel(let):
    if (let =="a" or let =="e" or let =="i" or let =="o" or let =="u" or let =="A" or let =="E" or let =="I" or let =="O" or let =="U"):
        print("Given letter is a Vowel")
    else:
        print("Given letter is NOT a Vowel")
def addtion(a,b):
    total = 0
    total = a+b
    print("the sum is :",total)

def subtraction(a,b):
    total = 0
    total = a-b
    print("the subtraction is :",total)

def multiplication(a,b):
    total = 0
    total = a*b
    print("the multiplication is :",total)

def division(a,b):
    total = 0
    total = a/b
    print("the division is :",total)

def printFactors(no1):
    print("The factors are")
    num = int(no1)
    fact = []
    for i in range (1,num):
        if (num % i == 0):
            fact.append(i)
        
    print("factors of the number are:",fact)

def printAllNum(no1):
    allnum = []
    i = 1
    while (i<= no1):
        allnum.append(i)
        i = i + 1
    print("print all nums:",allnum)

def printAllNumReverse(no1):
    allnum = []
    #i = no1
    while (no1 != 0):
        allnum.append(no1)
        no1 = no1 - 1
    print("print all nums in reverse:",allnum)




def main():
    print("Please enter the letter to check if it is a vowel or not:")
    char1 =input()
    checkVowel(char1)
    print("Please enter no1 :")
    no1 = int(input())
    print("Please enter no2 :")
    no2 = int(input())
    addtion(no1,no2)
    subtraction(no1,no2)
    multiplication(no1,no2)
    division(no1,no2)
    printFactors(no1)
    printAllNum(no1)
    printAllNumReverse(no1)



if __name__ == "__main__":
    main()
