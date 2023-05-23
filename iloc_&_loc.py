#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

data = {'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'], 'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'], 'Age': [30, 40, 25, 35, 45, 28], 'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'], 'Salary': [50000, 60000, 45000, 55000, 70000, 55000], 'Experience': [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)


#la méthode iloc pour sélectionner les 3 premières lignes
selection_iloc = employee_df.iloc[:3]
print("Sélection des 3 premières lignes (iloc):\n", selection_iloc)

#la méthode loc pour sélectionner toutes les lignes où le département est "Marketing"
selection_loc = employee_df.loc[employee_df['Department'] == 'Marketing']
print("Sélection des lignes où le département est 'Marketing' (loc):\n", selection_loc)

#la méthode iloc pour sélectionner les colonnes Age et Gender pour les 4 premières lignes
selection_iloc_columns = employee_df.iloc[:4, [2, 3]]
print("Sélection des colonnes Age et Gender pour les 4 premières lignes (iloc):\n", selection_iloc_columns)

#la méthode loc pour sélectionner les colonnes Salaire et Expérience pour les lignes où le Sexe est "Homme"
selection_loc_columns = employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 'Experience']]
print("Sélection des colonnes Salaire et Expérience pour les lignes où le Sexe est 'Homme' (loc):\n", selection_loc_columns)


# In[ ]:




