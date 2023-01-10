## Exercise Conditions 1-  
# print if num1 or num2 is greater num1 = 335 num2 = 66
num1 = 335
num2 = 66

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is not greater than {num2}")

## Exercise Conditions 2-  
# check if number1 is greater than number 2 and print number1 is greater than number2 then check and if number 2 is greater than number 1 and print number2 is greater than number1 finally at the end if both conditions incorrect print number2 equals to number1
number1 = 66
number2 = 66

if number1>number2:
    print(f"{number1} is greater than {number2}")
elif number2>number1:
    print(f"{number2} is greater than {number1}")    
else:
    print(f"{number1} equals to {number2}")

## Exercise Conditions 3-  
# Compare those 2 numbers and write X greater than Y But be sure you are making the check for all the conditions

import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

# Compare the numbers to eachother 
if number1>number2:
    print(f"x={number1} is greater than y={number2}")
elif number2>number1:
        print(f"y={number2} is greater than x={number1}")
else: print(f"x={number1} is equal to y={number2}")

## Exercise Conditions 4-
# Compare those 2 numbers' absolute values and write X's absolute value greater than Y's absolute value Use abs function to do that
# eg.
# abs(-5) -> 5
# abs function makes all numbers positive

import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print(f"x's absolute value, {abs(number1)} is greater than y's absolute value, {abs(number2)}")
elif abs(number1) < abs(number2):
    print(f"y's absolute value, {abs(number2)} is greater than y's absolute value, {abs(number1)}")
else:
    print(f"x's absolute value, {abs(number1)} equals to y's absolute value, {abs(number2)}")