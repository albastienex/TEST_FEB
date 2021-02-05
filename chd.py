# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:22:36 2021

@author: T30518
"""


# In[105]:


get_ipython().system('python --version')


# In[106]:


import numpy as np


# In[107]:


CHD_coef = np.array([-7.7013, 0.0524, 0.6555, 0.0205, 0.6723, 0.2991])


# ## 男性

# In[108]:


male = np.array([1, 65, 1, 145, 1, 0])
import math 
male_logit = np.dot(CHD_coef, male)
m_CHD_prob = math.exp(male_logit ) / (math.exp(male_logit ) + 1)
male_logit, m_CHD_prob


# ## 女性

# In[109]:


female = np.array([1, 65, 0, 145, 1, 0])
female_logit = np.dot(CHD_coef, female)
f_CHD_prob = math.exp(female_logit ) / (math.exp(female_logit ) + 1)
female_logit, f_CHD_prob


# In[110]:


(m_CHD_prob - f_CHD_prob) / f_CHD_prob


# ### 抽煙

# In[111]:


smoker = np.array([1, 65, 1, 145, 1, 1])
smoker_logit = np.dot(CHD_coef, smoker)
s_CHD_prob = math.exp(smoker_logit ) / (math.exp(smoker_logit ) + 1)
smoker_logit, s_CHD_prob


# In[112]:


(s_CHD_prob - m_CHD_prob) / m_CHD_prob