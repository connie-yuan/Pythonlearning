#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open("births.csv", 'r')
text = f.read()
print(text)


# In[5]:


linebirth=text.split("\n")
print(linebirth)


# In[16]:


newbirth=[]
for line in linebirth[1:len(linebirth)]:
    eachline=line.split(",")
    newbirth.append(eachline)
    print(eachline)


# In[15]:


print(newbirth)


# In[ ]:




