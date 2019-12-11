import pandas as pd
import numpy as np
from jedi.refactoring import inline
from scipy import stats
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('cars.csv', header=None)
data.columns = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style',
                'drive-wheels',
                'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight',
                'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',
                'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

data.plot(figsize=(18, 5))  # figsize este marimea dreptunghiului unde este afisat graficul (latimea si lungi)
plt.show()

isNull = data.isnull().values.any()
print("Data is null -" + str(isNull))

data.head()

## data fara randuri si erori
data_fara_lipse = data.dropna()
data_fara_lipse.tail()

data.hist(figsize=(15, 20))

# ## Definirea problemei de regresie
#
# Dorim sa cumparam o masina in viiitor care va avea anumite specificatii (peak-rpm,horsepower,highway-mpg,engine-size)

dc = data[data['make'] == 'bmw']
# caracteristica (peak-rpm,horsepower,highway-mpg,engine-size) - variabila independenta x
X = dc[['peak-rpm', 'horsepower', 'highway-mpg', 'engine-size']]
# raspunsul Pretul masinii cu anumite proprietati
Y = dc['price']

model = LinearRegression()

scores = []
kfold = KFold(n_splits=3, shuffle=True, random_state=42)

Y = dc.as_matrix(['price'])

pretMediuMasina = model.fit(X, Y)
prezicire = pretMediuMasina.predict(np.array([[6500, 80, 35, 209]]))

for i, (train, test) in enumerate(kfold.split(X, Y)):
    scores.append(model.score(X, Y))
print(scores)
print(prezicire)

# Concluzie

# In acest laborator am studiat regresia, astfel cu ajutorul acesteaia folosind diferite criterii putem prezice rezultatle viitoare,
# astfel in acest laborator pe baza unor caracteristici a masinilor am prezis pretul viitor a masinii.
