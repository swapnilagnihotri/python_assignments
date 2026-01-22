
def areaRectangle(length,breadth):
    area = length*breadth
    print("Area of rectangle is",area)

def areaCircle(radious):
    pi = 3.14
    area = pi*(radious**2)
    print("Area of a circle is:", area) 

def getFactors(no1):
    fact = []
    for i in range (1,no1):
        if (no1 % i == 0):
            fact.append(i)
    return fact  
    
def checkPerfectNum(no1):
    fact = getFactors(no1)
    sum = 0
    #i = 0
    for i in range(len(fact)):
        sum = sum + fact[i]
        i = i + 1
    print("sum of the factors is",sum)
    if (sum == no1):
        print("The number is perfect")
    else:
        print("The number is not perfect number")
    
def getBinary(no):
    binlist = []
    str1=""
    while (no>0):
        str1=str1+str(no % 2)
        no = no // 2
        
    print("Binary equivalent is:",str1)

def displayResult(marks):
    if(marks >= 75):
        print("Distiction")
    elif (marks >= 60 and marks <75):
        print("First Class")
    elif (marks >=50 and marks <60 ):
        print("Second class")
    elif (marks < 50 ):
        print("Fail")


def main():
    print("Enter length of a rectangle:")
    length = int(input())
    print("Enter breadth of a rectangle:")
    breadth = int(input())
    areaRectangle(length,breadth)
    print("Enter radious of a circle:")
    radious = int(input())
    areaCircle(radious)
    print("Enter the number to check if it is a perfect number or not:")
    num1 = int(input())
    checkPerfectNum(num1)
    print("Enter the number to find its binary equivalent:")
    num2 = int(input())
    getBinary(num2)
    print("Enter the marks to find teh result:")
    marks = int(input())
    displayResult(marks)




if __name__ == "__main__":
    main()