import matplotlib.pyplot as plt
import numpy as np

# Parametros de la orbita
a = 1  # Semi-eje mayor, 1UA (unidad astronimica) 
e = 0.0167  # excentricidad de la orbita terrestre 

# Coordenadas polares
θ = np.linspace(0, 2*np.pi, 1000) # Angulos de 0 a 2π
r = (a*(1-e**2))/(1+e*np.cos(θ)) # Valores de r

# Conversion de coordenadas polares a cartesianas
x = r*np.cos(θ)
y = r*np.sin(θ)

# Grafica
plt.plot(x, y)
plt.xlabel("Eje X")
plt.ylabel('Eje Y')
plt.title("Órbita elíptica")
plt.axis("equal")  
plt.grid(True)
plt.show()