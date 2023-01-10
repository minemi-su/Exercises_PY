### Exercise Methods 3
num1 = 1122334455666
# cast num1 to string and assign to num1_str
num1_str = str(num1)
# check the length of the string
len_of_str = len(num1_str)
print(len_of_str)
# get the third element of string (the one in the 3rd order)
num2=num1_str[2]
# get the 3-5 elements of string (both inclusive) by string slicing
num3=num1_str[3:6]
# check if num2 in string (cast if necessary)
print(num2 in num1_str, type(num2))
# check if num3 in string (cast if necessary)
print(num3 in num1_str, type(num3))
# concatenate 0 to the string from left and assign to string_with_0
string_with_0 = ('0'+num1_str)
# get the characters of string_with_0 from start to position 4 (end point exclusive)
print(string_with_0[:4])
# get the characters of string_with_0 from position 5 until the end
print(string_with_0[5:])
# use negative indexing to reach the "567" string_with_0
print(string_with_0[-9:-6]) #I hope I understand this correctly