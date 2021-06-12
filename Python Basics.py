#!/usr/bin/env python
# coding: utf-8

# In[ ]:


results = []
for i in range(2000,3201):
    if((i % 7) == 0 and (i % 5) != 0):
        results.append(i)
        
results


# In[20]:


first_name = input()
second_name= input()


# In[22]:


first_name_str = ''
for i in first_name:
    first_name_str = i + first_name_str
second_name_str = ''
for i in second_name:
    second_name_str = i + second_name_str
print(first_name_str + ','+second_name_str)


# In[23]:


print((4/3)  * 3.14 * (12**3))


# In[ ]:




