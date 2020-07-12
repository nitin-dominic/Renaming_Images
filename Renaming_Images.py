#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
# Function to rename multiple files
def main():
   i = 1650
   path=r"C:/Users/nitin/OneDrive/Desktop/Python_Algorithms/Dataset_Preparation/train/black_grass/"
   for filename in os.listdir(path):
      my_dest ="image000" + str(i) + ".png"
      my_source = path + filename
      my_dest = path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()


# In[ ]:




