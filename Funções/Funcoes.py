#!/usr/bin/env python
# coding: utf-8

# ## Exercícios - Métodos e Funções

# In[1]:


# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      
def imprimePar():
    tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    for i in tp:
        if i % 2 == 0:
            print (i)
            
imprimePar()


# In[ ]:





# In[17]:


# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def letraR(tex):
    return tex.upper()

letraR('Finalmente consegui resolver esse problema')


# In[ ]:





# In[ ]:


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista


# In[27]:


def addList (lista):
    print(lista.append(76))
    print(lista.append(8))
    
list1 = [1, 2, 3, 4]
addList(list1)
print(list1)


# In[32]:


addList(list1)


# In[33]:


# Cálculadora Salário
def calculadora_salario(valor, horas=220):
    return horas * valor

valor_total = calculadora_salario(299.25)

print(valor_total)


# In[35]:


calculadora_salario(20)


# In[ ]:





# In[ ]:


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos


# In[36]:


def trabArgs (arg1, *args):
    print(arg1)
    for i in args:
        print(i)
    return;


# In[39]:


trabArgs(29)
trabArgs(29,'ana', 'teste')


# In[10]:


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
#Para criar uma função anomina utilizamos o "lambda"


soma = lambda num1, num2: num1 + num2
print('A soma é: ',(soma(30,20)))


# In[ ]:





# In[17]:


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local

total = 0   #aqui temos uma variável global
def soma( arg1, arg2 ):
    total = arg1 + arg2; #dentro da nossa função chama-se por variável local e não é uma boa pratica usar o mesmo nome 
#na variavel local e global
    print ("Dentro da função o total é: ", total) #variável local
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total) #variável global

#Quando eu chamo a função 'SOMA' ela vai executar o código que está dentro da função que eu criei, realizando a operação de
#atribuir a variável local chamada "TOTAL" a soma entre arg1 e arg2 (total=arg1+arg2). Porém se eu chamar apenas a variavél 
#"TOTAL" no meu código (print(total)) será retornado o valor da variável global.
#Como uma boa pratica de código não devemos atribuir o mesmo nome para variável global e local.
#Para melhor compreensão do código, poderíamos deixar da seguinte maneira:

total = 0
def soma (arg1, arg2):
    soma_total = arg1 + arg2;
    print('O valor da soma é: ', soma_total)
    return soma_total;

soma (1,2)
print('O valor da minha variável global: ', total)

#Dessa forma, o código fica mais limpo e podemos evitar futuros bugs e confusões mentais


# In[ ]:





# In[5]:


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print (list(Fahrenheit))


# In[ ]:





# In[1]:


# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário
dicionario = {'key1': 'ano', 'key2': 'mês'}
dir(dicionario)


# In[6]:


# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
import pandas as pd
dir(pd)


# In[ ]:




