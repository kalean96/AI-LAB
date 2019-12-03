import pandas as pd
import numpy as np
from pandas import DataFrame, Series

csv = pd.read_csv('C:\\Users\\asus\\PycharmProjects\\untitled\\imbd_superhero.csv',
                  header=None,
                  names=['An', 'Titlu', 'Organizatia', 'IMBD', 'AltRating', 'DataX', 'UnknownColumn', 'PretMediulaBilet', 'NrDeSpectatori', 'TopPentruAncutare']
                  )

newline = '\n------------------------------------------------'

csv.head()
# 1 Creem o serie pandas
film = Series(csv['Titlu'])
# 2 Creem un dataFrame pandas
altFilm = DataFrame(csv['Titlu'])
print(altFilm)
print(film)
print(newline)
# 3 afisam doar filmelele de la DC
print(csv[csv['Organizatia'] == 'DC'])
# 4 afisam anul si titlul filmelor de la Marvel
new_csv = csv.loc[csv['Organizatia'] == 'Marvel']
title_and = new_csv[['An', 'Titlu']]
print(title_and)
print(newline)
