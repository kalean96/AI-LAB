#!/usr/bin/env python
# coding: utf-8

# # Arborele de decizie

# Un <b>arbore de decizie</b> este o structură de arbore asemănătoare unui flux în care un <b>nod intern</b> reprezintă o caracteristică (sau un <b>atribut</b>), ramura reprezintă o <b>regulă de decizie</b> și fiecare <b>nod frunză reprezintă rezultatul.</b>

#  Cel mai înalt nod dintr-un arbore de decizie este cunoscut sub numele de <b>nod rădăcină.</b> Învață pe baza valorii atributului.  

# Această structură ajută în luarea deciziilor.

# Vizualizarea este o diagramă care imită cu ușurință gândirea umană. <b>Arborii de decizie</b> sunt ușor de înțeles și de interpretat.

# 
# <img src="files/tree.jpg">

# ### Arborele de decizie este un tip de algoritm numit <b>'cutie albă'</b>. 

# Acesta împărtășește logica de luare a deciziilor interne, care nu este disponibilă în tipul de algoritmi <b>'cutie neagră'</b>, precum Rețelele Neurale.

# Timpul său de <b>antrenare/învățare</b> este mai rapid în comparație cu algoritmul rețelelor neuronale. Complexitatea în timp a arborilor de decizie este o funcție a numărului de înregistrări și a numărului de atribute din <b>datele de învățare.</b> 

# </b> Arborele decizional este o metodă fără distribuție care nu depinde de presupunerile de distribuție a probabilității. 

# #### Arborii de decizie pot trata <b>colecții mari de date</b>  cu o precizie bună.
# <br>

# # Cum funcționează algoritmul Arbore de decizie?

# Ideea de bază din spatele oricărui algoritm de arbore de decizie este următoarea:

# 1. Selectați cel mai bun atribut folosind o <b>Metrică de selecție a atributelor</b> pentru a împărți observările.
# 2. Faceți din acel atribut un nod de decizie și  împărțiți setul de date în subseturi mai mici.
# 3. Construiți arborele prin repetarea procesului din pasul 2 recursiv pentru fiecare copil până când:
# <ul>
# - Nu mai există alte atribute.
# - Nu mai există observații în setul de date.
# </ul>

# <img src="files/flow.jpg">

# # Metrica de selecție a atributelor

# Metrica de selecție a atributelor (MSA) este o <b>euristică</b> pentru selectarea criteriului de împărțire a datelor în cea mai bună manieră posibilă. Este, de asemenea, cunoscută sub numele de <b>regulă de divizare.</b>

# MSA oferă o notă fiecărei caracteristici (sau atribute) explicând setul de date dat.

# Atributul cu cel mai mare scor va fi selectat ca atribut de divizare.

# Cele mai populare metrici de selecție sunt: 
# - <b>câștigul de informație (pe baza entropiei) - Algorimtul ID3,</b> 
# - raportul de câștig, 
# - indicele Gini

# # Construirea arborelui de decizie în Scikit-learn

# ### Importăm librăriile necesare

# In[1]:


# Încărcarea librăriilor
import pandas as pd # Dataframe-ul și series-ul nostru
from sklearn.tree import DecisionTreeClassifier # Importăm Clasificatorul „Arborele decizional”
from sklearn.model_selection import train_test_split # Importăm funcția de separare a datelor în date de antrenare și date de testare
from sklearn import metrics #Importăm modulel metrici pentru caluclarea acurateții


# ### Importăm setul de date
# 

# Eu voi lucra cu <b>weather.csv</b> - clasic pentru această problemă.
# Fiecare își va alege setul de date dorit (la fel ca și în laboratorul anterior).

# In[2]:


# încărcarea setului de date
weather = pd.read_csv("data/weather.csv")
weather


# ### Transformăm exemplele din setul de date în valori numerice dacă este cazul

# In[3]:


from sklearn import preprocessing # preprocesarea datelor
from sklearn.preprocessing import OrdinalEncoder # functie care transforma din date categorice in numere
enc = preprocessing.OrdinalEncoder()

# caută legitate în date
enc.fit(weather)  

# transformă după legea găsită într-un array
data = enc.transform(weather)

# punem datale noatre înapoi în dataframe
weather = pd.DataFrame({'outlook': data[:, 0], 'temperature': data[:, 1], 'humidity': data[:, 2], 
                       'windy': data[:, 3], 'play': data[:, 4]})
weather


# ### Selectarea caracteristicilor

# In[4]:


#despărțim datasetul în vector de caracteristici (features) și vectorul clasă
features = ['outlook', 'temperature', 'humidity', 'windy']
X = weather[features] # caracteristicile (atributele pentru X)
y = weather.play # Variabila clasă (independentă dacă facem analogie cu regresia)


# ### Împărțirea setului de date
# Pentru a evalua performanța modelului o strategie ar fie împărțirea setului de date în: date de antrenare/învățare și date pentru testare/evaluare.
# 
# Putem face acest lucru utilizând funcția train_test_split(). Funcția ia 3 parametri: caracteristicile, clasa și lungimea setului de date pentru testare.

# In[7]:


# Împărțim setul de date în train set și test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% pentru antrenare and 30% testare
X_test


# ### Construirea modelului

# In[6]:


# Crearea obiectului de clasificare pe bază de arbore de decizie cu parametru criterie
clasificator = DecisionTreeClassifier(criterion="entropy")

# Antrenarea clasificatorului cu datele noastre utilizând metoda fit() și ca parametru avem datele de antrenare
clasificator_arbore_decizie = clasificator.fit(X_train,y_train)


# ### Evaluarea modelului

# In[8]:


#Prezice clasele pentru setul de testare utilizând metoda predict(parametru_setu_de_testare)
y_prezis = clasificator_arbore_decizie.predict(X_test)


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_prezis))
print(y_test, y_prezis)


# In[13]:


obiect_nou = X_test[X_test["outlook"] == 1.0]
clasificator_arbore_decizie.predict(obiect_nou)


# ### Vizualizarea arborelui

# Puteți folosi funcția export_graphviz din Scikit-learn pentru a afișa arborele în Jupyter Notebook. Pentru a face diagram de asemenea este nevoie de biblioteca pudotplus.
# Pentru instalarea clasică:
# 
# - pip install graphviz
# 
# - pip install pydotplus
# 
# funcția export_graphviz transformă clasificatorul nostru intr-un fișier cu puncte, iar pydotplus convertește aceste puncte într-un fișier png.

# In[14]:


from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clasificator_arbore_decizie, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True, feature_names = features,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('weather.png')
Image(graph.create_png())

