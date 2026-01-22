# Assignment 4:
#1. what is the difference between list and tuple in terms of mutability,memory,performance, use cases
#Answer: List are mutable where as tuples are not.List requires more memory as the size is not fixed where as tuple have fixed size.Tuples are faster as they are immutable as compare to list
# List can be used where input is dynamic, data is getting modified. tuples acan be used where fixed set of input without any modification is required.
# it is faster


#2. Why tuples are faster than list? In what real world scenario would you prefer a tuple over a list?
# Answer: List is mutable, user can add,update delete values within it. So it requires additional information to keep track of this info
# Tuples are not mutable so it does not required to store any additional info. So tuples are faster. It can be used where data is fixed,where read only data needs to be provided.

#3. predict the output and tell which line will raise the error,
lst = [10,20,30]
tpl = (10,20,30)
lst[0] = 100
tpl[0] = 100

#Answer: step#3 will update lst 0th position value from 10 to 100. Step#4 will give an error as tpl is immutable so its value cannot be updated

#4. Explain why strings are immutable in python,what happens internally when you modify a string variable?
#Answer: String sre used widely.python uses small strings and integers objects repeatedly saving memory.it is imjutable so can be safely used in multi threaded env.abs
# If you try to modify a string variable it creates a new string object internally instead of modifying exiting one.

#5. predict the output and explian the reason for change/no change in id().
# s = "Python"
# print(id(s))
# s= s + "3"
# print(id(s))

#Answer: id will change as we have updated the existing string so internally it has created a new object with new id

#6. what is the dictionary in python. Explain:-key-value pair,why keys must be immutable,why duplicate keys are not allowed,
# Answer: Disctionary is data type , it is unordered,can be traverse using keys.keys should be string since the are immutable ,values can be any other data type like int,str,etc.
# Keys should be unique.

# dict abc{
#     "name":"Ganesh",
#     "age": 26
# }

# name and age are keys and ganesh and 26 are values.python calculates hash from keys so kesy acannot be duplicate or muttable so they are made up of strigs.

#7 predict the output : d = {1:"one",1:"ONE",2:"two"} print(d)
# Answer : it will fail as key needs to be unique and here 1 is repeated with different values.

#8. what is range data type in python? How it is different from list of number.
# Answer: it a build in data type and is a squence of number. Usually used in for loop , it has 3 elements start-from where to start the iteration
#  ,stop- till stop-1 iterate the loop, step - by how much number next step should be incremented.by default it is 1.
# e.g. for 1 in range(2,10,2) . This means iterate i from 2nd element till 9th element and everytime increase the iteration number by 2
# List does not have step option

#9. predict the output:
# r = range(5)
# print(r)
# print(list(r))
# Answer: print(r) will print the range from 0 to 5. print(list(r)) will print 0 to 4 in the form of list

#10 . what is the difference between range(1,10) and range(1,10,2)
#answer: range (1,10) means start iteration from 1st position and not 0th position and iterate till 9, range(1,10,2) means start iteration from 1st position and not 0th position and iterate till 9 and in evry iteration increate the count by 2
