## Iterators - While Loop
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

## Iterators - For Loop
# Create
# *
# ***
# *****
# this shape with print, for loop, if and continue statements
for i in range(1,6):
    if i%2==0:
        continue
    else: print("*"*i)

## Iterators - For Loop
# Check if it is time for coffee break if it is just break
# To do that lets iterate through given list don't change the COFFEE BREAK statement.
# just find another way to do it
todo = ["exercise1", "exercise2", "exercise3","coffee break", "exercise4","exercise5","exercise6"]
for x in todo:
    if x.upper() == "COFFEE BREAK":
        print(x)
        break