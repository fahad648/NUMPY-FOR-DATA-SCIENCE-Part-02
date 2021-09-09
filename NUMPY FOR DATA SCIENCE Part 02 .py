#!/usr/bin/env python
# coding: utf-8

# ## M.FAHAD FAROOQ 

# # NUMPY INDEXING AND SELECTION :

# In[1]:


import numpy as np


# In[2]:


arr=np.arange(0,11)


# In[3]:


arr


# In[4]:


arr[5:]


# In[5]:


arr[4]


# In[6]:


arr[:5]


# In[7]:


slic=arr[:5]


# In[8]:


slic


# # How Numpy Array Differ From Python List :

# ## Numpy Is Different From Pyhton List Because Of Its Broadcasting Behaviour

# In[9]:


slic[:5]=100


# In[10]:


slic


# ### See Due to its Boradcasting Behaviour its also changes the Orignal Array   As well as Slic Array 

# In[11]:


arr


# ### But This Boradcast will not affect the Copy Array See :

# In[12]:


copy_arr=arr.copy()


# In[13]:


copy_arr


# In[14]:


copy_arr[:]=200


# In[15]:


copy_arr


# #### See The Orignal Array Got Un-Affected :

# In[16]:


arr


# ## Creating 2d Array and Some Indexing Func : 

# In[18]:


arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[19]:


arr1


# #### DOUBLE BRACKET METHOD TO GRAB  ANY ELEMENT FROM ARRAY 

# In[24]:


arr1[0][3]


# In[25]:


arr1[1][2]


# In[26]:


arr1[2][0]


# #### SINGLE BRACKET METHOD TO GRAB  ANY ELEMENT FROM ARRAY 

# In[27]:


arr1[0,3]


# In[28]:


arr1[1,2]


# In[29]:


arr1[2,0]


# ### SLICING METHOD TO GRAB CHUNK OF ARRAY  

# In[30]:


arr1


# In[31]:


arr1[:2,1:]


# In[32]:


arr1[0:,:2]


# In[34]:


bool_arr=arr1>5


# In[35]:


bool_arr


# In[39]:


arr1[bool_arr]                       #it will give only those values which are correct 


# # NUMPY OPERATIONS 

# In[40]:


arr1=np.arange(11,22)


# In[41]:


arr1


# In[42]:


arr1*arr


# In[43]:


arr1-arr


# In[44]:


arr1+arr


# In[45]:


arr1/arr


# In[46]:


arr1/11


# In[47]:


arr1+100


# In[48]:


arr1-100


# In[49]:


arr1/0


# In[50]:


0/arr1


# In[51]:


arr1**3


# In[53]:


arr1/9


# In[54]:


np.sqrt(arr1)


# In[55]:


np.exp(arr1)


# In[56]:


np.max(arr1)


# In[57]:


np.min(arr1)


# In[ ]:




