#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import matplotlib.pyplot as plt
x=np.random.random(100)
#print(x)


# In[24]:


plt.hist(x,10)

plt.xlabel("x value")
plt.ylabel("y value")
plt.show()


# In[25]:


mu,sigma=0,0.1 #令平均值跟標準差
s=np.random.normal(mu,sigma,10000)
plt.hist(s,10)
plt.show()


# In[26]:


ss=plt.hist(s,10)
print(ss)


# In[27]:


bins=np.linspace(-0.5,0.5,21,endpoint=True)
print(bins)
plt.hist(s,bins)
plt.show()


# In[28]:


import math
h=6.62*10**-34
c=3*10**8
k=1.38*10**-23
num=100
v=np.linspace(10**0,10**15,num,endpoint=True)
T=5500.
B=2*h*v**3/c**2/(math.e**(h*v/k/T)-1)

plt.plot(v,B,".")

dB=np.random.normal(0.,10**-8.5,num)
B+=dB
plt.plot(v,B)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




