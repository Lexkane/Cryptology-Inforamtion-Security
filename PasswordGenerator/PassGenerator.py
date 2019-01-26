#-------------------------------------------------------------------------------
# Name:        Password Generator
# Purpose:     Random PasswordGenerator input length of password and get password
# Author:      LK
# Created:     24.10.2018
# Copyright:   (c) LK 2018
# Licence:     GNU Licence
#-------------------------------------------------------------------------------

import random
lis=[]
length=int(input("Enter length of the password:"))
b=input("Would you like to use special characters?Y/N")

def PassGen(length):
 for j in range(length):
  lis.append(chr(random.randint(33,121)))
 print (*lis)
 print("lol1")

def PassGenWithoutSpecial(length):
 while (length>0):
   a=random.randint(33,121)
   if ((a>47 and a<58)or (a>64 and a<91) or (a>96 and a<123)):
     lis.append(chr(a))
     length-=1
 print(*lis)


def main():
    if (length > 0):
        if (b == "Y" or b=="y"):
            PassGen(length)
        elif (b == "N" or b == "n"):
            PassGenWithoutSpecial(length)
        else:
            print("Please input Y/N")
    else:
        print("Please input valid length")

if __name__ == '__main__':
    main()