# convert num1 to float and assign to itself
num1 = 1.3
num1=float(num1)  #I try to do as in tutorials: num1=num1.float() but can't reach that attribute, so I did this instead
# convert num2 to int and assign to itself
num2 = 2.3
num2 = int(num2)
# convert num3 to complex and assign to itself
num3 = 1j
num3 = complex(num3)
# use round method for num4 and assign to itself
num4 = 1.4 
num4 = round(num4)
# use round method for num5 and assign to itself
num5 = 1.5
num5 = round(num5,2) # will not going to change anything
num5 = round(num5)
# print them all
print("num1:",num1,", num2:",num2,", num3:",num3,", num4:",num4,", num5:",num5)
 # print their types
print("type of num1:",type(num1),", type of num2:",type(num2),", type of num3:",type(num3),", type of num4:",type(num4),", type of num5:",type(num5))