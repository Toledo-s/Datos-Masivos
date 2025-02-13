import numpy as np
from sklearn.linear_model import LinearRegression

X =np.array([[4], [6], [7], [8], [9], [11]])
y =np.array([9,7,6,5,3,1])

model = LinearRegression()
model.fit(X, y)

prediccion = model.predict([[2]])

print(f"Horas productiva: {prediccion[0]} miles de dólares")   
