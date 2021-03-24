#!/usr/bin/env python
# coding: utf-8

# # Calculadora

# In[ ]:


print ('*********************Python Calculator*************************\n')

print ('Selecione a opção desejada: \n \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão')

escolhe = input ('Digite sua opção (1/2/3/4): ')

if escolhe == '1': 
    
    num1 = input ('Digite o primeiro número: ')
    num2 = input ('Digite o segundo número: ')
    soma = int(num1) + int(num2)
    print (str(soma))
    
elif escolhe == '2':
    num1 = input ('Digite o primeiro número: ')
    num2 = input ('Digite o segundo número: ')
    subtrai = int(num1) - int(num2)
    print (str(subtrai))

elif escolhe == '3':
    
    num1 = input ('Digite o primeiro número: ')
    num2 = input ('Digite o segundo número: ')
    multiplica = int(num1) * int(num2)
    print (str(multiplica))
    
elif escolhe == '4':
    
    num1 = input ('Digite o primeiro número: ')
    num2 = input ('Digite o segundo número: ')
    divide = int(num1) // int(num2) 
    print (str(divide))
    
else:
    
    num1 = input ('Digite o primeiro número: ')
    num2 = input ('Digite o segundo número: ')
    print ('Opção Inválida')


# In[ ]:




