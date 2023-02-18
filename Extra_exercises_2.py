# extra exercises - 2 
## 1-An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
test_armstrong = input ('enter a number :')
if type(test_armstrong) is int:
    test_len = len(str(test_armstrong))
    test_a = str(test_armstrong)
    i=1
    test_value = 0
    while i<test_len+1:
        test_value = test_value+ (int(test_a[i-1])**test_len)
        i+=1
    else: 
        if test_value==test_armstrong:
            print('the number is an armstrong number') 
        else:
            print('this is not an armstrong number')


# 2- Determine if a sentence is a pangram or not , A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once.
import string
alphabet = set(string.ascii_lowercase)
len_a=len(alphabet)
i=0
sentence = str(input('enter a sentence: '))
sentence = set(sentence.lower())
while i>len_a: 
    if alphabet[i] in sentence:
        i+=1
    elif i==27: 
        print('this sentence is a pangram')
    else:
        print('this is not a pangram')