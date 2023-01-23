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
# Iterate each elements of list1,tuple1,set1 and print them out 
# For the dict1 iterate all elements but only print the ones who are living on land in the form of x lives in y
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
