#!/usr/bin/env python
# coding: utf-8

# ## Exercícios

# In[2]:


# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        


# In[16]:


roc1 = Rocket(2, 4)
roc1.x
roc1.y
roc1.print_rocket()
roc1.move_rocket(3, 5)
roc1.print_rocket()


# In[ ]:





# In[50]:


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa ():
    
    def __init__ (self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return "Nome: %s , Cidade: %s, Telefone: %s, Email: %s "     %(self.nome, self.cidade, self.telefone, self.email)
    
    def __len__(self):
        return self.telefone
    


# In[51]:


#criando um objeto

Pessoa1 = Pessoa('Amanda', 'Fortaleza', 859999999999, 'amanda@xxxxxx.com')
Pessoa1


# In[52]:


Pessoa1.nome


# In[53]:


Pessoa1.cidade


# In[54]:


Pessoa1.telefone


# In[55]:


Pessoa1.email


# In[56]:


str(Pessoa1)


# In[59]:


len(Pessoa1)


# In[ ]:





# In[61]:


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.


class Smartphone():
    
    def __init__ (self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface


# In[62]:


class MP3Player(Smartphone):
    
    def __init__ (self, capacidade):
        self.capacidade = capacidade


# In[63]:


#criando um objeto

mp2 = MP3Player(30)


# In[64]:


mp2


# In[ ]:





# In[ ]:





# ### FIM

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
