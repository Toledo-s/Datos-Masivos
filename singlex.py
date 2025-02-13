import numpy as np
from sklearn.linear_model import LinearRegression

X =np.array([[5,80,70], [6,85,75], [7,90,80], [8,95,85], [9,100,90], [10,100,92], [11,95,88], [12,90,85]])
y =np.array([75,80,85,90,95,98,92,89])

model = LinearRegression()
model.fit(X, y)

prediccion = model.predict([[6,50,60]])

print(f"Nota final: {prediccion[0]} miles de dólares")   
