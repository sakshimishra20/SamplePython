#!/usr/bin/env python
# coding: utf-8

# In[1]:


def about_me(your_name):
    print("The wise {} loves Python.".format(your_name))            

def HW():
    print("Hello World!")

def Both():
    HW()
    about_me("Ab")

Both()
F  = open(r"a.txt", "a")
F.write("ok\n")


# In[ ]:




