#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
workPath = '/home/jovyan/workspace'
if not workPath in sys.path:
    sys.path.append(workPath)


# In[2]:


import everest


# In[3]:


import h5py
import os
import numpy as np


# In[4]:


IC = everest.examples.myobject2.build(400.)
system = everest.examples.myobject1.build(a = 1, b = 0.5, initial_time = IC)


# In[5]:


outputPath = '..'
name = 'test'
extension = 'h5'
path = os.path.join(outputPath, name + '.' + extension)
if everest.mpi.rank == 0:
    if os.path.exists(path):
        os.remove(path)


# In[6]:


system.anchor(path)


# In[7]:


for i in range(10):
    system.go(10)
    system.store()
system.stored


# In[8]:


system.save()


# In[9]:


system.stored

if everest.mpi.rank == 0:

    h5file = h5py.File(path)


    print(h5file[system.hashID]['var'][...])


    h5file.close()


# In[13]:


# loadsystem = everest.built.load_built_from_h5(path, system.hashID)

