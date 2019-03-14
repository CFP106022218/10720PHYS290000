#!/usr/bin/env python
# coding: utf-8

# In[32]:


import random
import math
import numpy as np
import matplotlib.pyplot as plt
pigx=(random.randint(1,40))
pigy=(random.randint(1,10))

V=20
angle=45
g=-9.8;
Vx=V*math.cos(angle*math.pi/180);
Vy=V*math.sin(angle*math.pi/180);

t=np.arange(0,-2*Vy/g,0.01)
Xx=t*Vx;
Xy=Vy*t+0.5*g*t*t;
plt.plot(Xx,Xy)
plt.plot(pigx,pigy,"o")


# In[36]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.image as mpimg

im=mpimg.imread('P1120107.JPG')


# In[37]:


import matplotlib.pyplot as plt
plt.imshow(im)


# In[38]:


print(im.shape)


# In[39]:


r_im=im[:,:,0]
plt.imshow(r_im)


# In[41]:


plt.imshow(r_im,cmap="Greys")


# In[42]:


plt.hist(r_im.ravel())


# In[46]:


import numpy as np
print(np.mean(r_im))
print(np.median(r_im))


# In[ ]:




