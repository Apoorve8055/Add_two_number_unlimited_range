# -*- coding: utf-8 -*-
"""
@author: Apoorv verma
@Apoorve8055
"""

str1 = input("enter the number : ")
str2 = input("enter the number : ")
len1 ,len2 = len(str1),len(str2)
maxval = max(len1,len2)
str3 = "" 
i = 0
carry = 0
while i != maxval :
    if (len1 -1 - i) < 0:
        num1 = 0
    else:
        num1 = str1[len1 -1 - i]
    if (len2 -1 - i) < 0:
        num2 = 0
    else:
        num2 = str2[len2 -1 - i]
    d1 = int(num1)
    d2 = int(num2)
    if carry == 1 :
       sum1 = d1 + d2 + 1
    else:
       sum1 = d1 + d2 
    if (sum1) > 9:
        amt = (sum1) - 10;carry = 1
        str3 = str3 + str(amt)
    else:
        carry = 0
        str3 = str3 + str(sum1)
    i = i + 1
print(str3[::-1])
