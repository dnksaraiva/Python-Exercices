#!/usr/bin/env python
# coding: utf-8

# ## Exercícios 

# In[ ]:


'''Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
Cria uma função que calcule a terceira potência'''

def potenciaC(item):
    return item ** 3


# In[ ]:


#cria uma lista 

numeros = [4, 5, 6]


# In[ ]:


#Chama a função map que retorna a potência de cada elemento da sequência(lista)
#O resultado será um iterator, para corrigir esse problema você deve transformar esse iterator em uma lista

map(potenciaC, numeros)


# In[ ]:


#Transformando o iterator em lista

list(map(potenciaC, numeros))


# In[ ]:





# In[19]:


# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)


# In[ ]:


palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()


# In[6]:


palavras


# In[16]:


def palaV(L):
    return (L.upper(), L.lower(), len(L))


# In[17]:


map(palaV,palavras)


# In[18]:


list(map(palaV,palavras))


# In[ ]:





# In[ ]:





# In[35]:


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
transposta = [[row[i] for row in matrix] for i in range(2)]
print(transposta)


# In[ ]:





# In[46]:


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def potenciA(A):
    return A ** 2

def potenciB(B):
    return B ** 3

print (list(map(potenciA,lista)) + list(map(potenciB,lista)))


# In[54]:


# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [2, 3, 4]

list(map(pow, listaA,listaB))


# In[64]:


# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)

list(filter(lambda x: x < 0), range(-5, 5))


# In[ ]:


# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

list(filter(lambda x: x in a,b))

# In[ ]:


# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

import time
print(time.strftime("%d/%m/%Y %H:%M:%S"))


# In[ ]:


# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}


# In[ ]:


# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

