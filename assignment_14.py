# 1 .write a lambda function which accepts one number and returns its square
# 2 .write a lambda function which accepts one number and returns its cube
# 3 .write a lambda function which accepts two number and returns maximum number
# 4 .write a lambda function which accepts one number and returns minimum number
# 5 .write a lambda function which accepts one number and returns True if the number is even otherwise false 
# 6 .write a lambda function which accepts one number and returns True if that number is odd otherwise false
# 7 .write a lambda function which accepts one number and returns True if it is divisible by 5
# 8 .write a lambda function which accepts one number and returns its addition
# 9 .write a lambda function which accepts one number and returns its multiplication
# 10 .write a lambda function which accepts 3 numbers and returns largest


getSquare = lambda No:(No*No)
getCube = lambda No:(No**3)
getMaxNum = lambda No1,No2:(No1 if No1 > No2 else No2)
getMinNum = lambda No1,No2:(No1 if No1 < No2 else No2)
CheckEven = lambda No:(No % 2 == 0)
CheckOdd = lambda No:(No % 2 == 1)
DivisiblebyFive = lambda No:(No % 5 == 0)
Addition = lambda No1,No2:(No1 + No2)
Multiplication = lambda No1,No2:(No1 * No2)
getLargest = lambda No1,No2,No3:(No1 if No1 > No2 and No1 > No3 else (No2 if No2 > No3 else No3))


def main():
    no = 0
    no1 = 0
    no2 = 0
    ans = 0
    #check1 = False

    no = int(input("Enter the number to find its square,cube,even,odd,dividible by 5 :"))
    ans = getSquare(no)
    print("Sqaure is :", ans) 
    ans = getCube(no)
    print("Cube is :", ans) 
    ans = CheckEven(no)
    print("CheckEven is :", ans) 
    ans = CheckOdd(no)
    print("CheckOdd is :", ans) 
    ans = DivisiblebyFive(no)
    print("DivisiblebyFive is :", ans) 

    no1 = int(input("Enter first number :"))
    no2 = int(input("Enter second number :"))
    

    ans = getMaxNum(no1,no2)
    print("Max number is :",ans)

    ans = getMinNum(no1,no2) 
    print("Min number is :", ans) 

    ans = Addition(no1,no2)
    print("Addition is :", ans)

    ans = Multiplication(no1,no2)
    print("Multiplication is :",ans)

    no3 = int(input("Enter thrid number for to find larget amoung 3 numbers :"))
    ans = getLargest(no1, no2, no3)
    print("Largest number is:",ans)

    
if __name__ == "__main__":
        main()

