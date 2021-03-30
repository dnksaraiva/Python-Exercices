#!/usr/bin/env python
# coding: utf-8

# # Banco de dados com SQLite

# In[1]:


import sqlite3


# In[2]:


#conecta ao banco de dados e caso ele não exista, será criado
con = sqlite3.connect('C:\Projects\Python-Exercises\SQLite\estudantes')


# In[3]:


#verifica a conexão
type(con)


# In[4]:


# Criando um cursor 
# (Um cursor permite percorrer todos os registros em um conjunto de dados)
cur = con.cursor()


# In[33]:


#criando uma instrução SQL

sql_create = 'create table cursos ''(id integer primary key, ''titulo varchar(1000), ''categoria varchar(100))'


# In[ ]:





# In[6]:


# Executando a instrução sql no cursor
cur.execute(sql_create)


# In[7]:


type(cur)


# In[8]:


# Criando outra sentença SQL para inserir registros
sql_insert = 'insert into cursos values (?, ?, ?)'


# In[9]:


datas1 = [(1, 'Maria Paula Cruz', 'Moda'),(2, 'Juliana Freire', 'Enfermagem')]


# In[14]:


for item in datas1:
    cur.execute(sql_insert, item)


# In[15]:


#Gravando os Dados
con.commit()


# In[16]:


# Criando outra sentença SQL para selecionar registros
sql_select = 'select * from cursos'


# In[17]:


# Seleciona todos os registros e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall()


# In[24]:


# Mostra
for linha in dados:
    print ('Curso Id: %d, Nome: %s, Categoria: %s \n' % linha)


# In[25]:


# Gerando outros registros
recset = [(3, 'Claudia Freire', 'Big Data'),
          (4, 'Arcrebiano', 'Análise de Dados')]


# In[26]:


for item in datas1:
    cur.execute(sql_insert, item)


# In[27]:


con.commit()


# In[32]:


# Seleciona todos os registros
cur.execute('select * from cursos')

# Recupera os resultados
datas1 = cur.fetchall()

# Mostra
for item in datas1:
    print ('Curso Id: %d, Nome: %s, Categoria: %s \n' % item)


# In[ ]:


#fechando a conexao
con.close()

