#!/usr/bin/env python
# coding: utf-8

# # Laborator 3. Regresia Liniara in Python utilizand Pandas si Scikit-Learn
# #

# ## Cuprins
#
# 1. Selectarea setului de date.
# 2. Importarea bibliotecilor si setului de date.
# 3. Studierea setului de date.
# 4. Setarea problemei si Pregatirea setului de date pentru antrenare.<br>
#    a. Divizare in set de date pentru antrenare si set de date pentru testare. <br>
#    b. Utilizarea k-folds cross validation pentru testare.
# 5. Initializarea modelului de regresie liniara si aplicarea acestuia pe datele noastre.
# 6. Concluzii.

# ## Selectarea setului de date
# 1. Setul de date il veti alege de sine stator din urmatoarele repositorii (important este ca setul de date sa fie compatibil cu rezolvarea problemei de regresie liniara):<br>
#    a. https://archive.ics.uci.edu/ml/datasets.php?format=&task=&att=&area=&numAtt=&numIns=&type=&sort=taskDown&view=table <br>
#    b. https://www.kaggle.com/rtatman/datasets-for-regression-analysis <br>
#    c. https://data.world/datasets/regression <br>
#    d. https://www.kdnuggets.com/datasets/index.html
# 2. Creati un fisier de tip jupyter notebook in aceeasi mapa.
#
# ### Cei care nu-si gasesc nimic potrivit pot folosi acelasi dataset folosit anterior (lab. 2).
# ### Exemplul va fi pe datasetul utilizat in lab. 2.
#

# ## Importarea bibliotecilor si setului de date

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# incarcam fisierul .csv intr-un dataframe |
# daca la voi nu e csv, incercati mai intai sa-l transformati in csv
#

# In[3]:


data = pd.read_csv('C:\\users\\Asus\\Projects\\Testing\\src\\day.csv', header=None)
# nu avem setate numele de coloane |
# in lab 2 le-am setat direct in fctia read_csv utilizand atributul names='' |
# insa le putem seta si dupa incarcarea fisierului
data.columns = [
     "instant",
     "dateday",
     "season",
     "year",
     "month",
     "holiday",
     "weekday",
     "workingday",
     "weathersit",
     "temp",
     "atemp",
     "hum",
     "windspeed",
     "casual",
     "registered",
     "cnt"
]

# ## Studierea setului de date prin manipularea acestuia

# Hai sa vizualizam datele, grafic

# In[4]:


data.plot(figsize=(18, 5))  # figsize este marimea dreptunghiului unde este afisat graficul (latimea si lungimea)

# Daca privim mai atent datele putem observa niste lucruri stranii in grafic
# 1. Se pare ca anumite date lipsesc (acolo unde este sters graficul)
# 2. Se pare ca avem anomalii in date. (anumite date nu coincid cu valorile de min sau max care le poate lua o coloana)

# Pentru a verifica daca nu lipsesc unele valori in setul nostru de date folosim fctia isnull()
#

# In[5]:


data.isnull().values.any()

# Functia a returnat <b> True </b> ceea ce inseamna ca trebuie sa analiam si sa vedem ce date lipsesc

# In[6]:


# afisarea tabelara primelor date din tabel
data.head()

# Observam anumite date cu valoarea <b>NaN</b> (Not a Number) in coloanele <i>UnkColumn</i> si <i>NrDeSpectatori</i> care, probabil, ne pun piedica. <br>
# O metoda ar fi sa scapam de aceste valori prin a sterge randurile unde ele apar.<br>
# Putem aceste randuri utilizand functia dropna(). <br>
# Functia dropna() sterge randul unde cel putin un element lipseste sau este diferit de valoare coloanei.<br>
# Functia folosita pe coloane, ex. dropna(axis='column'), sterge coloana unde cel putin un element lispste.

# In[4]:


## data fara randuri cu erori
data_fara_lipse = data.dropna()
data_fara_lipse.tail()

# ## Anomalii in anumite coloane (Muntii din grafic)

# Anomaliile din date sunt niste valori extreme ale unor caracteristici. <br>
# Valorile extreme, de obicei, apar in rezulatatul unui experiment eronat, sau chiar poate fi o valoare corecta.
# Cel mai bine este sa le stergem.

# In[5]:


data.hist(figsize=(15, 20))

# ## Definirea problemei de regresie
#

# Presupunem ca vrem la anul sa mergem la un film de la DC si vrem sa cunoastem care va fi pretul mediu la bilet.

# Drept urmare, din datele noastre putem lua ca si o caracteristica din observarile anterioare pentru variabila independenta x - coloana "An", iar drept raspuns variabila dependenta y - coloana "PretMediulaBilet"

# In[6]:

XY = data[['holiday', 'cnt']]
# caracteristica an - variabila independenta x
X = data['holiday']
# raspunsul Pretul mediu la bilet - variabila dependenda y
Y = data['cnt']
print(str(X.count() == Y.count()) + " <- daca true, avem acelasi numar de observatii")  ## daca true, avem acelasi numar de observatii
n = X.count()
print("Numarul de observatii este %d intre %2.3f si %2.3f " % (n, X.iloc[0], X.iloc[n - 1]))
print()
# functia .iloc [] este bazata in principal pe pozitia intreaga (de la 0 la lungimea-1 a coloanei).
#

# In[7]:


XY.plot.scatter(y='cnt', x='holiday')

# In[8]:


XY.corr()
# XY.descibe()


# In[9]:


model = LinearRegression()

# In[10]:


scores = []
kfold = KFold(n_splits=3, shuffle=True, random_state=42)

# In[12]:


X = data.as_matrix(['holiday'])
Y = data.as_matrix(['cnt'])

# In[212]:


# In[15]:


atemp_model = model.fit(X, Y)
atemp_model.predict(np.array([[0]]))

print(atemp_model.predict(np.array([[0]])))

data_a = data[data['holiday'] == 1]

print(data_a.mean())

# In[20]:


Y[:5]

# In[221]:


for i, (train, test) in enumerate(kfold.split(X, Y)):
    scores.append(model.score(X, Y))
print(scores)


# In rezutatul efectuarii lucrarii am inteles lucrul cu regresia liniara si cum putem prezice vre-un eveniment
# bazandu-ne pe date din precedent;
# In lucrare am utilizat dataset al turneelor biciclistilor care in dependenta de timpul de afara sau zilele saptamanii
# variaza prezenta la eventiment, si am prezis numarul de prezenta intr-o zi de sarbatoare
