## ESERCIZI PYTHON
# Exercise 1
#Create two tuples representing the two lists of first and last names described below:
# names: Numa, Tullio, Anco;
# surnames: Pompilio, Ostilio, Marzio
# Get a list in which each element is a dictionary {'first name': first name, 'last name': last name},
# which matches first and last names according to order.

names = ('Numa','Tullio','Anco')
surnames= ('Pompilio', 'Ostilio', 'Marzio')
list_exc_1= list(zip(names,surnames))
print(type(list_exc_1),list_exc_1)

#  Exercise 2
# Create a dictionary that contains as keys 'name' and 'surname', entering their data as values.
# Add 'serial number' 
# Add 'exams', trying to imagine what types of data to use to represent both name and grade of the exams

student_dict={'name':'Mine','surname':'Su'}
student_dict['serial number']= 11111
student_dict['exams']=[{'Class':'Python','Grade':'75'},{'Class':'SQL','Grade':'70'}]
print(student_dict)


# CONDITIONALS - 1
# Write a program that: take a keyboard input string, representing a nucleotide (A, C, G, T) 
# print the complementary nucleotide on screenthe complementary nucleotide are (A,T) and (C,G) (in both ways) 
# Make sure the program works correctly with both uppercase and lowercase input.

nucleotide = input('enter a nucleotide (A,C,G,T): ')
nucleotide = nucleotide.upper()
if nucleotide == 'A':
    print('T')
elif nucleotide == 'C':
    print('G')
elif nucleotide == 'G':
    print('C')
elif nucleotide == 'T':
    print('A')
else: print('This is not a nucleotide. \n There are four nucleotides, in DNA: adenine (A), cytosine (C), guanine (G), and thymine (T)')

## CONDITIONALS Exercise -2 
# LEAP YEAR

year = int(input('enter the year: '))
if year%4==0 and year%100==0 and year%400==0:
    leap = True
else: leap=False
print((f"is the year {year} a leap year? \n {leap} "))

## ITERATIONS
# Exercise 1
# Calculate the sum of the first 500 natural numbers (from 0 to 500 excluded)
total_500= 0
for i in range(0,500):
    total_500+=i
print(total_500)
## Exercise 2
# Write a program that prints the length of the strings supplied by the user, until the user enters the string 'exit'
while True:
    string=input("enter a string : ").lower()
    if string == 'exit':
        break
    else:
        print(str(len(string)))
## Create a list containing 20 random integers in (0, 100) (0 included), print the number of even elements and the number of elements greater than 70.
import random
printable=[]
number_of=0
a_list=[random.randint(0,100) for _ in range(0,20)]
for i in a_list:   
    if i%2==0:
        printable.append(i)
    if i>70:
        number_of+=1
print(f"the even numbers in the list are : {printable}" , f"and the number of elements greater than 70 are : {number_of}")

##  Exercise 4
# Sort the elements in the guest list. Then, sort it in the opposite order.
# guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer'
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests=guests.sort()
sorted_guests=guests.sort(reverse=True)
print(guests)

## Exercise 1
# Write a function to determine the highest number in a list of integer (do not use the max() function).
import random
new_list=[random.randint(0,100) for _ in range(0,30)]
max=0
for i in range(len(new_list)):
    if new_list[i]> max
        max=new_list[i]
print(f"the highest number of the list is {max}")
print(f"the whole list is : {new_list}") 

## Exercise 2
# Write a function that given a list of integers, create another list containing only the elements of even position of the first list.
# will write on top of last exercises list "new_list"
even_list=[]
for i in new_list:
    if i%2==0:
        even_list.append(i)
print(f"the list of even numbers in previous list is: {even_list}")

## Exercise 3
# Write a lambda function that takes x as a parameter and returns x+2. Then assign it to a variable named L.
x=0
L=lambda x : x+2
print(L(x=10))