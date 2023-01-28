## 01 Iterators - While Loop
# Create ` * ** 
# the py file inside the exercise is below, but the website it says "Create ` * **" they are side by side, will write that version also 
# ver01
i = 1 
while i <6:
    print("*"*i)
    i = i + 1
# ver02
result=""
i=0
while i<6:
    result+=" "+("*"*i)
    i = i + 1
print(result)

## 02 Iterators - For Loop
# Create
# *
# ***
# *****
# this shape with print, for loop, if and continue statements
for i in range(1,6):
    if i%2==0:
        continue
    else: print("*"*i)

## 03 Iterators - For Loop
# Check if it is time for coffee break if it is just break
# To do that lets iterate through given list don't change the COFFEE BREAK statement. just find another way to do it 
# I'm not sure that I understood this but here is a solution acoording to hints
todo = ["exercise1", "exercise2", "exercise3","coffee break", "exercise4","exercise5","exercise6"]
for x in todo:
    if x.upper() == "COFFEE BREAK":
        print(x)
        break

## 04 Iterators - For Loop
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
# print the lengths of list1,tuple1,set1,dict1
print('lenght of list1 is ', len(list1),'\n','lenght of tuple1 is ', len(tuple1),'\n','lenght of set1 is ', len(set1),'\n','lenght of dict1 is ', len(dict1))
# print the first element of list1 and tuple1
print('first element of tuple1 is: ', tuple1[0],'\n','first element of list1 is: ', list1[0])
# print the value of lion key of dict1
print('value of lion key is: ', dict1['lion'])
# change the 2nd position element of list1 to "rabbit"
list1[1]="rabbit"
# try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
# tuple1[2] = "rabbit" 
# # I get a type error: tupple object does not support item assignment / tupple values can not be changed after creation  
# add "monkey" to list1
list1.append("monkey")
# remove "rabbit" from list1
list1.remove("rabbit")
# in dict1 the number of feet is written as value to each animal the fixh has wrong value just fix it.
# I did not understand the question but, did they imply lenght of their habitat  
dict1["fish"]="ocean"
dict1["fish"]=""

# Iterate each elements of list1,tuple1,set1 and print them out 
print("elements of list1 :",list1,"\n elements of tuple1 :",tuple1,"\n elements of set1 :",set1)
# For the dict1 iterate all elements but only print the ones who are living on land in the form of x lives in y
keys_of_dict1=list(dict1.keys())
for x in keys_of_dict1:
        if dict1[x]=="land":
            print(f'{x} lives in {dict1[x]}')
#just discovered another way
for x,y in dict1.items():
    print(f'{x} lives in {y}')    
## Exercise 1 - Functions
# create a function named goodbye without parameters which prints good bye
def goodbye():
    print("good bye")
goodbye()
## Exercise 2 - Functions
# create a function named goodbye with a parameter name and say "Good bye Adam"
def goodbye(name):
    print(f'Good bye {name}')
goodbye("Adam")
## Exercise 3 - Functions
# what is your user name on your computer
import os
user=os.getlogin()
print(user)


