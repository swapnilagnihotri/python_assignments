#1 write a program to display value ,type and memmory address for a variable using build in function

#var1 ="Jai Ganesh"
#print(type(var1))
#print(id(var1))

#2 what is the difference between a=10,b=10 and a=[10],b=[10]explain using id
#a = 10 # this has store integer in a 
#print(id(a))  #this will display address of variable
#b =10 # this has store integer in b
#print(id(b)) #this will display address of variable 
#a = [10] # this has created an object of list and stored 10 at 0th position
#print(id(a)) # this will print address of variable
#b = [10]  # this has created an object of list and stored 10 at 0th position
#print(id(b))  # this will print address of variable

#3 what does id() function return? is the valure returned by id() same for two variables holding the same value?
#Ans - id fucntion returns memory address.No value returned will be diferentif two variables holding same value.

#4 what is the purpose of getsizeof()? Why memory size is different for different data types
# purpose of getsizeof() is to get the size of the object.Data types are used for different purposes so as per requirment user can choose best suited data type.It varies as per programming languages
# 

# 5 a=10,b=10 print(id(a)===id(b))  
# this will print true as a and b bot hrefer to same integer object
 
#6 write a program which assepts two numbers from user and prints their addition,subtraction,multiplication and division

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

def main():
    print("Please enter no1 :")
    no1 = int(input())
    print("Please enter no2 :")
    no2 = int(input())
    addtion(no1,no2)
    subtraction(no1,no2)
    multiplication(no1,no2)
    division(no1,no2)
    # take user name and age and display the message 'hello <name>, you will turn <age+1> next year.
    print("Please enter you name :")
    name = input()
    print("Please enter your age :")
    age = int(input())
    print("Hello "+name +","+"you will turn "+str(age+1)+" next year")



if __name__ == "__main__":
    main()

#7 why does the input() function always return a string? How can you convert it into the other data type?
#answer: instead of guessing what is the data type given by user to the input function it is better to return it as a string and let the user interprte and typecast it into other data types if required

#8 predict the output x = input("enter number"),print(type(x))
# answer: as mentioned in above quetion input always returns string so the print will eturn <class str>

#9 write a program to take user and and age and display 'hello <name>, you will turn <age+1> next year.

# what is the out put of  print("10"+"20") and print(10+20)
#answer : print("10"+"20")  # this will print 1020 as both are in double quoates and are treated as strings, print(10+20) will print addition of two numbers i.e. 50