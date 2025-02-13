import numpy as np
from sklearn.linear_model import LinearRegression

X =np.array([[,,], [,,], [,,], [,,], [,,], [,,], [,,], [,,]])
y =np.array([,,,,,,,])

model = LinearRegression()
model.fit(X, y)

prediccion = model.predict([[,,]])

print(f"Lorem: {prediccion[0]} ipsum")   
