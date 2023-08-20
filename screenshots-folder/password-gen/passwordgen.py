import random as ran
import string as str 

def gen():
    #generate random strings
    s1 = str.printable

    #ask for length of password
    paslen = int(input("Enter lenght of password: \n"))

    #add the random stings to an empty list
    s = []
    s.extend(list(s1))

    #shiffle the values in the list
    ran.shuffle(s)

    #pass the values of the list to the password variable wirh regards to the length entered
    pas = ("".join(s[0:paslen]))
    print(pas)
1212

gen()