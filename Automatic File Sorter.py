#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter in File Explorer

# In[1]:


import os, shutil


# In[24]:


path = r"C:/Users/Montalvo/OneDrive/Desktop/automatic_file_sorter/"


# In[25]:


file_name = os.listdir(path)


# In[32]:


folder_names = ['excel files','image files','text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
        
for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "excel files/" + file):
        shutil.move(path + file, path + "excel files/"+ file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/"+ file)
    elif ".docx" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/"+ file)


# In[31]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




