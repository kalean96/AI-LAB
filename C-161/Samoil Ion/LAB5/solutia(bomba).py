import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#incarcam setul de date
iris = pd.read_csv("dataset/iris.csv")
#despărțim datasetul în vector de caracteristici (features) și vectorul clasă
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = iris[features] # caracteristicile (atributele pentru X)
y = iris.species # caracteristica clasă
#impartim setul de date integral in date de antranare si date de testare utilizand functia train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
'''
print("\n70% Antrenare:")
print(X_train)
print(y_train)
print("\n30% Testare:")
print(X_test)
print(y_test)
'''
#cream clasificatorul k-nn
#setam numarul de vecini ca parametru explicit
knn = KNeighborsClassifier(n_neighbors=5)
#antrenam modelul utilizand setul de date de antrenare
knn.fit(X_train, y_train)
#prezicem raspunsul corect pentru setul de destare
print("Raspunsurile date de model:")
y_pred = knn.predict(X_test)
print(y_pred)
