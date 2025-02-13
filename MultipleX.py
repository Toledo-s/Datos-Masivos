import numpy as np
from sklearn.linear_model import LinearRegression

X =np.array([[,,], [,,], [,,], [,,], [,,], [,,], [,,], [,,]])
y =np.array([,,,,,,,])

model = LinearRegression()
model.fit(X, y)

prediccion = model.predict([[6,50,60]])

print(f"Nota final: {prediccion[0]} miles de dólares")   
