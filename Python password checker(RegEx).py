#!/usr/bin/env python
# coding: utf-8

# In[15]:


# first Checker
import re
password = input("Enter Your password: ")
if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
     print("match")
else:
    print("no match")


# In[20]:


# Second Checker
import re
password = input("Enter Your password: ")
if re.match(r'[A-Za-z0-9@#$%^&+=]{7,}\d', password):
     print("match")
else:
    print("no match")

