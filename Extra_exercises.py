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