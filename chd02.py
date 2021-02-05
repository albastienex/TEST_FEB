# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:24:06 2021

@author: T30518
"""


import math 
y = 1
p = 0.8
-y*math.log(p) - (1-y) *math.log( 1 - p)


# In[116]:


y = 1
p = 0.9
-y*math.log(p) - (1-y) *math.log( 1 - p)


# In[117]:


import numpy as np
np.arange(0.55, 0.96, 0.1)


# In[118]:


np.vstack((np.arange(0.55, 0.96, 0.1),-y* np.log(np.arange(0.55, 0.96, 0.1)) - (1-y) * np.log( 1 - np.arange(0.55, 0.96, 0.1))))


# In[119]:


t = np.linspace(0.01, 0.99, 100)
positive_case = - np.log(t)
negative_case = - np.log(1 - t)
plt.plot(t, positive_case, 
         label="blue -log(t), red -log(1-t)")
plt.legend(loc="upper center", fontsize=12)
plt.plot(t, negative_case, "r-")
plt.grid()
plt.xlabel("p")
plt.savefig('data/lec06 log')
plt.show()


# In[120]:


t = np.linspace(-5, 5, 100)
fx = t**2 + 3
inverse_fx = -t**2 - 3
plt.plot(t, fx, t, inverse_fx)
plt.grid()
plt.show()