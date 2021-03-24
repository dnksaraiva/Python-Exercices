#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#calculadora em python, criando funções

print('****************Python Calculator********************\n')


#definindo as funções



def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x // y



print ('Escolha uma das opções: \n \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n ')

escolha = input ('Escolha uma operação (1/2/3/4):')

num1 = int (input ('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))

if escolha == '1':
    print(add (num1, num2))

elif escolha == '2':
    print (sub(num1, num2))

elif escolha == '3':
    print (mult(num1, num2))

elif escolha == '4':
    print (div(num1, num2))
    
else:
    print ('Opção inválida!')


# In[ ]:





# In[ ]:




