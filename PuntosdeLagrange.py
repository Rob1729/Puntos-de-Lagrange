import numpy as np
import matplotlib.pyplot as plt

M1= 1.989e30  # Masa del sol
M2= 5.972e24  # Masa de la tierra
d = 1.496e11  # Distancia Tierra-Sol (m)
mu= M2/(M1 + M2) #Correccion de la masa 


def PL1(d, M1, M2):
    return d*(1-np.cbrt(mu/3))

def PL2(a, M1, M2):
    return d*(1+np.cbrt(mu/3))

# Datos y Coordenadas de los puntos de Lagrange L1 y L2
x = np.linspace(0, 2e11, 100)
L1= PL1(d, M1, M2)
y1= 0

L2= PL2(d, M1, M2)
y2= 0

# # Coordenada del punto L3
L3= d*(1+mu)

# Coordenadas de los puntos de Lagrange L4 y L5
θ= np.pi/3  
x_L4= d*np.cos(θ)
y_L4= d*np.sin(θ)
x_L5= d*np.cos(θ)
y_L5= -d*np.sin(θ)

# Graficacion de los puntos de Lagrange
plt.plot(L1, y1, "ro", color="red", label="L1")
plt.plot(L2, y2, "ro", color="orange", label="L2")
plt.plot(-L3, 0, "ro", color="pink" , label="L3")
plt.plot(x_L4, y_L4, "ro", color="olive" , label="L4")
plt.plot(x_L5, y_L5, "ro", color="black" , label="L5")

# Graficacion de los cuerpos celestes
plt.plot(0, 0, "o", color="yellow", label="Sol")
plt.plot(d, 0, "o", color="blue", label="Tierra")

plt.title("Gráfico de puntos de Lagrange")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)
plt.show()