import numpy as np
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt

df = pd.read_csv( 'D:\Downloads\Libro1.csv')
 
print(df.head( ))  
#Case sensitive
X = df[[ 'Peso' , 'Altura']]. values  
y = df[ 'Etiqueta']. values 

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X,y)

nuevo_punto = np.array([[175,13]])
prediccion = knn.predict(nuevo_punto)
print(f"La fruta es clasificada como: {'Manzana' if prediccion == 0 else 'pera'}")