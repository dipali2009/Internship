#!/usr/bin/env python
# coding: utf-8

# Q-11.Write a python program to find the factorial of a number.
# 

# In[7]:


# To take input from the user

num = int(input("Enter a number: "))


# In[8]:


factorial = 1


# In[9]:


# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[ ]:


#12. Write a python program to find whether a number is prime or composite


# In[5]:


num = int(input("Enter any number : "))


# In[6]:


if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# In[ ]:


13. Write a python program to check whether a given string is palindrome or not.


# In[5]:


st = input("Please enter your own text : ")


# In[6]:


if(st == st[:: - 1]):
   print("This is a Palindrome String")
else:
   print("This is Not")


# In[ ]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.


# In[1]:


from math import sqrt


# In[ ]:


a=input("Enter a: ")


# In[ ]:


b=input("Enter b: ")


# In[ ]:


c=sqrt(a**2+b**2)


# In[ ]:


print("The lenght of hypotenuse is", c)


# In[ ]:


#Write a python program to print the frequency of each of the characters present in a given string


# In[10]:


str1 = input ("Enter the string: ")


# In[11]:


d = dict()
for c in str1:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(d)


# In[ ]:




