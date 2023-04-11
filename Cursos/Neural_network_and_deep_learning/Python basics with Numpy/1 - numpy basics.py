#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math

array = np.array([1, 2, 3])
y_hat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])


# In[ ]:


def math_sigmoid(x):
    return 1 / (1 + math.exp(-x))

print(math_sigmoid(1))


# In[ ]:


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

print(sigmoid(array))


# In[ ]:


def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s) 

print(sigmoid_derivative(array))


# In[ ]:


def image2vector(image):
    return image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)

#image = np.array([ [np.random.random(3)], [np.random.random(3)], [np.random.random(3)]])
image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])
        
print(image2vector(image))


# In[ ]:


def normalizeRows(x):
    return x / np.linalg.norm(x, axis = 1, keepdims = True)

#array = np.array([np.random.random(3), np.random.random(3)])
array = np.array([[0, 3, 4], [1, 6, 4]])

print(normalizeRows(array))


# In[ ]:


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis = 1, keepdims = True)

#array = np.array([np.random.random(5), np.random.random(5)])
array = np.array([[9, 2, 5, 0, 0], [7, 5, 0, 0 ,0]])
print(softmax(array))


# In[36]:


def L1(y_hat, y):
    return sum(abs(y - y_hat))
        
print(L1(y_hat,y))


# In[39]:


def L2(y_hat, y):
    x = y - y_hat
    return np.dot(x,x)

print(L2(y_hat,y))

