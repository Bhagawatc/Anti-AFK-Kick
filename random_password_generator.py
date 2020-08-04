import math
import string
from random import *

length = input("How long would you like the password?")

print(length)

 
letter_list_lowercase = list(string.ascii_lowercase)
letter_list_uppercase = list(string.ascii_uppercase)

print(letter_list_lowercase)
print(letter_list_uppercase)


ints = []
seed(1)     
for x in range(int(length)):
    value = random.randint(0, length)
    ints.append(value)

pwd = ''
end = False

while(end == False):
    if(pwd.__len__ == length):
        end = True
    else:
        for char in length:
            pwd.append(letter_list_lowercase[value[char]])


print(pwd)
