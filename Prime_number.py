'''
Created on Mar 10, 2018

@author: ITAUser
'''
num=int(input("Enter a positive number greater than 0: "))

if num > 1:
 
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")