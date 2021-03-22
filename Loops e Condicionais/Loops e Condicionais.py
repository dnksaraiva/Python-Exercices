#!/usr/bin/env python
# coding: utf-8

# # Exercícios

# In[6]:


# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
dia = input ('Qual o dia da semana?')
if (dia == 'Domingo') or (dia == 'Sábado'):
    print ('Hoje é dia de descanso!')
else:
     print ('Você precisa trabalhar!')


# In[5]:


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
list = ['banana', 'morango', 'uva', 'tomate', 'kiwi']
for fruta in list:
    if fruta == 'morango':
        print ('morango faz parte da lista')


# In[6]:


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
tp = ('ana', 'maria', 'melo', 'santos')
list = []
for i in tp:
    atualizacao = i * 2
    list.append(atualizacao)
print(list)


# In[7]:


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range (100,150,2):
    print(i)


# In[9]:


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
temperatura = 40 
while temperatura > 35:
    print(temperatura)
    temperatura = temperatura -1


# In[ ]:


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
contador = 0
while contador < 100:
    if contador == 23:
        break
    print(contador)
    contador = contador +1


# In[2]:


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
i = 4
atualizada = list()
while (i <= 20):
    atualizada.append(i)
    i = i + 2
print(atualizada)


# In[2]:


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
list(range(5, 45, 2))


# In[18]:


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.]


# In[3]:


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)
count = 0
frase = 'É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir.'
for caracter in frase:
    if carecter == 'r':
        count = caracter + 1
        


# In[ ]:





# In[ ]:




