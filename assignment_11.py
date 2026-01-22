# Assignment 11:
# 1. write a program which accepts one number and checks whether it is prime or not
# 2. Write a programe which accepts one number and prints count of digits within that number
# 3. Write a programe which accepts one number and prints sum of digits within that number
# 4. Write a programe which accepts one number and prints reverse of digits within that number
# 5. Write a programe which accepts one number and checks whether it is palindrome or not

def checkPrime(no):
    # prime number means it should be divisible by 1 or itself -max 2 factors e.g 2,3,5,7,11,13 etc
    primeno = int(no)
    if (primeno <= 1):
        print("Given number is not prime number")
    else:
        for i in range(2,primeno):
            if(primeno % i == 0):
                print("The number is not prime")
            else:
                print("The number is prime")



def findNumberLength(no1):
    print("Length of the given number is:",len(no1))

def sumofDigits(no1):
    sum = 0
    for i in range(len(no1)):
        sum = sum + int(no1[i])
    print("Sum of digits of the given number is :",sum)

def reverseNum(no1):
    rev =""
    for i in range(len(no1)):
        rev = no1[i]+rev
    return rev


def main():
    print("Enter the number to find its length:")
    no = input()
    findNumberLength(no)
    sumofDigits(no)
    revNum = reverseNum(no)
    print("Reverse of the number is:",revNum)
    if (no == revNum):
        print("Given number is palindrom")
    else:
        print("Given number is NOT palindrom")
    checkPrime(no)
    


if __name__ == "__main__":
    main()
    
