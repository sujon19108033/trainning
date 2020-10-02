#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Practical example of comparison or relational operators in Python

# Trainer: Md. Jalal Uddin, Founder and director of Research Society https://researchsociety20.org/founder-and-director/
# email: dmjalal90@gmail.com, dmjalal90@nuist.edu.cn


# In[ ]:


# define variable

a = 5
b = 6


# In[ ]:


# comparison or relational operators by Syntax

print('If a is greater than b =',a>b)

print('If a is less than b =',a<b)

print('If a is equal to b =',a==b)

print('If a is not equal to b =',a!=b)

print('If a is greater than or equal to b =',a>=b)

print('If a is less than or equal to b =',a<=b)


# In[ ]:


# comparison or relational operators by Function

# import library
import operator as op

print('If a is greater than b =',op.gt(a,b))

print('If a is less than b =',op.lt(a,b))

print('If a is equal to b =',op.eq(a,b))

print('If a is not equal to b =',op.ne(a,b))

print('If a is greater than or equal to b =',op.ge(a,b))

print('If a is less than or equal to b =',op.le(a,b))


# In[ ]:


# Example for real data
# We will monitor drought for Rangpur station from 1994 to 1995
# The example has been adapted from Uddin et al. (2020). https://link.springer.com/article/10.1007/s12517-020-05302-0


# In[ ]:


# Importing the library

import pandas as pd


# Importing the dataset

dataset = pd.read_excel('comparison_or_relational_operators.xlsx')
#print(dataset)

SPI = dataset.SPI[133:156]   #1994-1995

print('SPI values = \n',SPI)


# In[ ]:


# comparison or relational operators by Syntax

print('Extreme drought   = \n',SPI<=-2)


# In[ ]:


# comparison or relational operators by Function

# define variable 
Threshold = -2

print('Extreme drought   = \n',op.le(SPI,Threshold))


# In[ ]:




