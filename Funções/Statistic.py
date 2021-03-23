#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"

def statisticDesc(file_name):
    df = pd.read_csv(file_name)
    return df.describe()
    
statisticDesc(file_name)  

