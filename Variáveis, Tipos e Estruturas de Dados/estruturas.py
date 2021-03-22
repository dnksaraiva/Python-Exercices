#!/usr/bin/env python
# coding: utf-8

# ## Exercícios Variáveis, Tipos e Estruturas de Dados

# In[ ]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.


# In[1]:


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[2]:


list


# In[ ]:





# In[ ]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela


# In[3]:


list1 = ['maçã', 'abacaxi', ' morango', 'uva', 'banana']


# In[4]:


list1


# In[ ]:





# In[ ]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string


# In[5]:


s1 = 'dani'


# In[6]:


s2 = 'kelle'


# In[7]:


s3 = s1+s2


# In[8]:


s3


# In[ ]:





# In[ ]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla


# In[9]:


tupla = (1, 2, 2, 3, 4, 4, 4, 5)


# In[10]:


tupla


# In[12]:


tupla.count(4)


# In[ ]:





# In[ ]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela


# In[15]:


dicionario = {}


# In[16]:


dicionario


# In[ ]:





# In[ ]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela


# In[17]:


dict1 = {'Danikelle': 21, 'Maria': 30, 'Julia': 25}


# In[18]:


dict1


# In[ ]:





# In[ ]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela


# In[20]:


dict1['Ana'] = 12


# In[23]:


dict1


# In[ ]:





# In[ ]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.


# In[24]:


dict2 = {'arroz': 5, 'feijao': 7, 'carne':[20,30]}


# In[25]:


dict2


# In[ ]:





# In[ ]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.


# In[28]:


list12 = ['carros', ('leite', 5), {'Ana': 20, 'Pedro': 22}, 4.5]


# In[29]:


list12


# In[ ]:





# In[ ]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'


# In[30]:


frase = 'Cientista de Dados é o profissional mais sexy do século XXI'


# In[32]:


frase[0:18]

