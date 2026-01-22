# Assignment 3:
#1. what is user defined function? Write a function to accept two numbers and return its multiplication
#Answer: user defind function is a written by programmer. It is a custom block of set of intructions which and be used repeatedly to avoid duplication of code.

def multiplication(a,b):
    total = 0
    total = a*b
    return total 

#2 what is the difference between a. function with parameter and b.function without parameter  .Give one example each.
#answer: 1 .Function with parameters: takes input values, flexible and reusable,can perform operations on different data. Above multiplication(a,b) is an example of of function with parameters
# function without parameter: does not take any input value, generally have internal logic and fixed values ,simple but less flexible
#below is example without parameter
#def JayGanesh():
 #   print("Jai Ganesh")

 # 3.predict the output 
# def fun():
#     x = 0
#     print(x)
# fun()
# print(x)

#Answer: Here flow will start from fun()->> def fun()-->local var x is set to 0->>print(x);x =0 is printed on console->> outside last print(x) will give error a x is not defined. Since x is defined locally in fun() its scope is limited to fun()

# 4: Write a function which does not return anything but prints message.Explain default value of such function.
# Answer: Here is an example,
#def JayGanesh():
 #   print("Jai Ganesh")
#  the default return value is 'None'

#5:what is the difference between print() and return.explain with function.

# def JayGanesh():
#     print("Jai Ganesh")
# This function will print Jai Ganesh on console. Its retrun type is none so does not sends anything back to caller.

# def multiplication(a,b):
#     total = 0
#     total = a*b
#     return total

# When function sends something back to the programmer it is sent in the form of return. This needs to be captured in some variable in the program for further processing

#6 write the program to display data type ,memory address,size in bytes of a variable entered by user
import sys
var = print("enter input",input())
print(id(var))
print(type(var))
print(sys.getsizeof(var))

#7 predict the output ,what feature it demonstrate
a = 5
print(type(a))
a =5.5
print(type(a))
a = " python"
print(type(a))

#answer: <class 'int'> , <class 'float'>,<class 'str'> , this demonstrate pythin is a dynamically typed language

#8: explain whty the following code works without declartion x = 100
# answer : User does not need to define data type of the variable. Since python is dynamically typed it decides the data type based on the value provided to it.a

# 9. What is the diference between x = 10 and x = "Ten"
# Answer: yes it is allowed as python is dynamically typed it decides the value of variable based on the input given. Here first int and then str are passed to x.capitalize

#10. Explain how python manages memory internally?Why does user not need to explicitly allocate or free memory
# Python uses automatic memory management. no need to allocate memory explicitly. When user defines variable python creates an object of teh same



