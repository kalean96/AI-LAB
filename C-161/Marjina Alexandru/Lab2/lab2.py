import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib
import inline
# get_ipython().run_line_magic('matplotlib', 'inline')

csv = pd.read_csv("imbd_superhero.csv",
                  header=None,
                  names=['An', 'Titlu', 'Organizatia', 'IMBD', 'AltRating', 'DataX', 'UnknownColumn',
                         'PretMediulaBilet', 'NrDeSpectatori', 'TopPentruAncutare'])
csv.head(8)

# Vedem multe valori NaN - Not a Nuber. In numpy este o functie care detecteaza aceste valori si le eilmina utilizand functia isfinite()

new_csv = csv[np.isfinite(csv.UnknownColumn)].append(csv[np.isfinite(csv.NrDeSpectatori)])

new_csv.head(8)

# vrem sa comparam coloanele imbd cu AltRating. pentru a face acest lucru trebuie sa normalizam datelele.

# Normalizam scorurile
imbd_normalizat = new_csv.IMBD / 10  # nota imbd din 10
new_csv.insert(10, 'IMBD_normalizat', imbd_normalizat)

altrating_normalizat = new_csv.AltRating / 100  # scorul din 100
new_csv.insert(9, 'AltRating_normalizat', altrating_normalizat)

new_csv.head()

# ### graficul, distributia si corelatii

# ## Graficul

new_csv.plot.scatter(y='IMBD_normalizat', x='AltRating_normalizat')

# ## corelare

# Putem vedea  din grafic o corelatie pozitiva dintre date. Ar fi bine totusi sa va verificam cat de puternica este corelatia. Pandas ofera o metada numita corr() pentru a calcula corelatiile.
# Nu trebuie sa facem acest lucru pentru intreg DataFrame-ul, ci numai pentru coloanele in cauza.

new_csv[['IMBD_normalizat', 'AltRating_normalizat']].corr()

# Am obtinut matricea de corelare. Corelarea este 0.888, una foarte buna. Similaritatea dintre note este foarte mare.

# ## Descrierea coloanelor

# Utilizand fucntia describe() din pandas putem afla informatie despre fiecare coloana in parte, precum media, devierea de la standard, etc.

new_csv[['IMBD_normalizat', 'AltRating_normalizat']].describe()

# ## Linia de tendita / trend

plot = new_csv.plot.scatter(x='An', y='PretMediulaBilet')
z = np.polyfit(x=new_csv.An, y=new_csv.PretMediulaBilet, deg=5)  # polinom de gradul 5 inseamna deg=5
p = np.poly1d(z)
trendline = pd.DataFrame(data=p(new_csv.An), index=new_csv.An)
trendline.plot.line(ax=plot, color='Yellow')

# De realizat:
# 1. Definiti o serie pandas.
# 2. Definiti un dataframe in pandas.
# 3. Cum veti afisa numai filmele de la DC pentru DataFrame-ul new_csv?
# 4. Cum veti afisa numai anul si titlu pentru filmele de la  Marvel?
# 5. Desenati graficul pentru PretulMediuLaBilet cu Anul pe axa y. Culoarea liniei sa fie neagra.


#Definesc seria
dataSeries = pd.Series(new_csv['An'])
print(dataSeries)
#Definisec dataframe

marvelData = new_csv[new_csv["Organizatia"]=="Marvel"][['Titlu','An']]

# marvelData =new_csv.where(filter)
# marvelData.dropna()
print(marvelData)

# print(marvelData['Titlu'],marvelData['An'])
# print(marvelData[['Titlu','An']])