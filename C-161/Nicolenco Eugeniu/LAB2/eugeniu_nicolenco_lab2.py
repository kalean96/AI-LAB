# author @Eugeniu Nicolenc

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

csv = pd.read_csv('C:\\Users\\asus\\PycharmProjects\\untitled\\imbd_superhero.csv',
                  header=None,
                  names=['An', 'Titlu', 'Organizatia', 'IMBD', 'AltRating', 'DataX', 'UnknownColumn', 'PretMediulaBilet', 'NrDeSpectatori', 'TopPentruAncutare']
                  )

newline = '\n------------------------------------------------------------'

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

# 5 cu plot nu s-a primit

# Concluzie
# Am reusit sa insusesc unele metode de lucru cu datele din pandas, am exersat un pic si cu max(), mean() etc
# Am reusit sa manipulez cu datele de parca ar fi un SQL si altfel