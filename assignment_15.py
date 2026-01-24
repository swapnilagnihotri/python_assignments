# 1. Write a lambda function using map() which accepts a list of numbers and return a list of squares of each number
# 2. Write a lambda function using filter() which accepts a list of numbers and return a list of even number
# 3. Write a lambda function using filter() which accepts a list of numbers and return a list of odd number
# 4. Write a lambda function using reduce() which accepts a list of numbers and return addition of all elements
# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum number
# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum number
# 7. Write a lambda function using filter() which accepts a list of strings and return a list of string having length greater than 5
# 8. Write a lambda function using filter() which accepts a list of numbers and return a list of numbers divisible by 3 and 5
# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements
# 10. Write a lambda function using filter() which accepts a list of numbers and return count of even numbers


from functools import reduce


def main():
    data = [1,2,3,4,5,6,7,8,9,10,15]
    print("Data",data)
    
    reSquare = list(map((lambda A:A**2),data))
    print("Squre list of given list is :",reSquare)

    listEven = list(filter(lambda A:A % 2 == 0,data))
    print("Even number list from given list is :",listEven)
 
    listOdd = list(filter(lambda A:A % 2 == 1,data))
    print("Odd number list from given list is :",listOdd)

    getAdd = reduce(lambda A,B:A + B,data)
    print("Addtion of all numbers within list is :",getAdd)

    getMax = reduce(lambda No1,No2:(No1 if No1 > No2 else No2),data)
    print("Max of all numbers within list is :",getMax)

    getMin = reduce(lambda No1,No2:(No1 if No1 < No2 else No2),data)
    print("Min of all numbers within list is :",getMin)

    getNumDivisibleby3n5 = list(filter(lambda A: A % 3 == 0 and A % 5 == 0,data))
    print("List of all numbers divisible by 3 and 5 is :",getNumDivisibleby3n5)

    strData = ["hi","hello","welcome","goodbye","a","good night","yahoo"]
    print("Prin strData", strData)

    getProduct = reduce(lambda A,B:A * B,data)
    print("product of all numbers within list is :",getProduct)

    getStingGreaterThan5 = list(filter(lambda A:len(A) > 5 ,strData))
    print("List of strings having length more than 5 is :",getStingGreaterThan5)
    
    getEvenCount = len(list(filter(lambda A:A % 2 == 0,data)))
    print("Count of even numbers within given list is :",getEvenCount)



if __name__ == "__main__":
    main()