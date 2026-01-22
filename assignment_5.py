# Assignment 5:

#1. what is bytes in python? why are they immutable?
#Answer : bytes is a immutable sequence of integers from 0-255. it stors several type of data like raw data, images, network packages. SInce it may contain 
# important data making it immutable assurs the data integrity, faster retrival and simplified memory management.

#2 predict the output: b = bytes([65,66,67]) print(b).Explain how numbers are converted internally?
# I do not know the answer ,wil lsearch

#3 What is the difference between bytes and bytearray?Mention mutability and use cases
#answer : bytes is immutable so faster and bytearray is mutable so slower than bytes.bytes is used for fixed data

#4 predict the output: 
ba = bytearray([65,66,67])
ba[0] =97
print(ba)
#answer aBC

#5 What is none in python? Is it same as 0,False or empty string?
#answer none is constant that has value none. it is not same as if you use type(none) it returns nonetype whereas rest returns int,bool n str

#6 predict the output:
x = None
print(type(x))
print(x == False)
#answer : line 24 will print Nonetype. #26 will print False as bool False got assinged to it in same call
