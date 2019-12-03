import pandas as pd  # Dataframe-ul și series-ul nostru
from sklearn.tree import DecisionTreeClassifier  # Importăm Clasificatorul „Arborele decizional”
from sklearn.model_selection import \
    train_test_split  # Importăm funcția de separare a datelor în date de antrenare și date de testare
from sklearn import metrics  # Importăm modulel metrici pentru caluclarea acurateții
from sklearn import preprocessing  # preprocesarea datelor
from sklearn.preprocessing import OrdinalEncoder  # functie care transforma din date categorice in numere
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

cars = pd.read_csv("cars_clas.csv", header=None)
cars = cars.dropna()
print(cars)

enc = preprocessing.OrdinalEncoder()

# caută legitate în date
enc.fit(cars)

# transformă după legea găsită într-un array
data = enc.transform(cars)

# punem datale noatre înapoi în dataframe
cars_data = pd.DataFrame({'make': data[:, 2], 'engine-type': data[:, 14], 'engine-size': data[:, 16],
                          'fuel-system': data[:, 17], 'horse-power': data[:, 21], 'peak-rpm': data[:, 22],
                          'price': data[:, 25], 'price_lvl': data[:, 26]})

print(cars_data)

# despărțim datasetul în vector de caracteristici (features) și vectorul clasă
features = ['make', 'engine-type', 'engine-size',
            'fuel-system', 'horse-power', 'peak-rpm',
            'price']
X = cars_data[features]  # caracteristicile (atributele pentru X)
y = cars_data.price_lvl  # Variabila clasă (independentă dacă facem analogie cu regresia)

# Împărțim setul de date în train set și test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=1)  # 70% pentru antrenare and 30% testare
print(X_test)

clasificator = DecisionTreeClassifier(criterion="entropy")

# Antrenarea clasificatorului cu datele noastre utilizând metoda fit() și ca parametru avem datele de antrenare
clasificator_arbore_decizie = clasificator.fit(X_train, y_train)

y_prezis = clasificator_arbore_decizie.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_prezis))
print(y_test, y_prezis)

obiect_nou = X_test[X_test["make"] == 2.0]
clasificator_arbore_decizie.predict(obiect_nou)

dot_data = StringIO()
export_graphviz(clasificator_arbore_decizie, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names=features, class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('cars.png')
Image(graph.create_png())
