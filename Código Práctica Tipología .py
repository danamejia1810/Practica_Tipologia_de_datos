#!/usr/bin/env python
# coding: utf-8

# 
# Vamos a utilizar las herramientas de Web Scrapping para la siguiente página y poder obtener la lista de los paises Suramericanos y las variables claves de su economía: https://en.wikipedia.org/wiki/South_America

# In[195]:


import requests


# Empezamos leyendo el código fuente de la página web y creando un objeto BeautifulSoup.
# 
# BeautifulSoup permite crear un árbol de análisis para las páginas que se buscan analizar y que se pueden usar para extraer datos de HTML.
# 
# La función prettify() en BeautifulSoup nos permitirá ver cómo se estructuran las etiquetas en el documento.

# In[196]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[197]:


title = soup.find(id="firstHeading")
title


# In[198]:


# Imprimimos el titulo de la página web
print(title.text)


# In[199]:


tables = soup.find_all("table", {"class":"wikitable sortable"})


# In[200]:


#En la página web podemos observar que la tabla que se desea extraer la información es la número 8
my_table = soup.find_all('table')[8]
print(my_table)


# In[201]:


# Buscamos todos los elementos 'th' en el cuerpo de la tabla, usando find_all():
th = my_table.find_all("th")
print(th)


# In[202]:


# Extraemos el título de los enlaces, para conocer los nombres de las columnas:
for i in range(len(th)):
  link = th[i].find("a")

  if link != None:
    print(link.get("title"))


# In[203]:


# Extraemos solo los valores de la tabla
mytable=soup.find_all('table')[8]
rows=mytable.find_all('tr')
rows=rows[1:-1]

c1=[]
c2=[]
c3=[]
c4=[]
c5=[]
c6=[]
c7=[]

for row in rows:
    x=row.find_all('td')
#    x=x[1].text
#    c1.append(x[:-1])
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    x5=x[4]
    x6=x[5]
    x7=x[6]
    c1.append(x1.text[:-1])
    c2.append(x2.text[:-1])
    c3.append(x3.text[:-1])
    c4.append(x4.text[:-1])
    c5.append(x5.text[:-1])
    c6.append(x6.text[:-1])
    c7.append(x7.text[:-1])
    
print(c2)
    


# In[204]:


import pandas as pd

df=pd.DataFrame()

df['Country']=c1
df['GPD_nominal']=c2
df['GDP_PPP']=c3
df['GDP_PPP_per_capita']=c4
df['Merchandise_exports']=c5
df['HDI']=c6
df['Percent_less_than_2']=c7

df


# In[205]:


# Exportamos la tabla a un archivo csv
df.to_csv("South_America_Economy.csv", index = False)


# In[ ]:




