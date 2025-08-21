#Problema 1

"""Cant de datos transmitidos(Megabytes)
Tiempo (Segundos)"""
from os import system
def limpiar():
    system("cls || clear")

def D(t):
    return 100*t 

minuto=round(1.5*60)

hora=60*60 #3600 Segundos
limpiar()
print("--- Problema 1 ---")
print(f"\nA los 45 segundos, se transmiten {D(45)} Megabytes.")
print(f"\nA los 1.5 minutos, se transmiten {D(minuto)} Megabytes.")
print(f"\nA la hora, se transmiten {D(hora)} Megabytes.\n")

#Problema 2
print("--- Problema 2 ---")
def tabla():
   for i in range (0,1100,100):
    print(f"{i} s: {D(i) } Megabytes")
tabla()

#Problema 3
print("\n--- Problema 3 ---")
def calcular_latencia_real(latencia_estimada):

    latencia_real = latencia_estimada * 1.20
    return latencia_real

latencias_estimadas = [200, 149, 74]

print("\nLatencia real calculada: ")
for latencia in latencias_estimadas:
    real = calcular_latencia_real(latencia)
    print(f"Latencia estimada: {latencia} ms -> Latencia real: {real:.2f} ms\n")

#Problema 4
print("--- Problema 4 ---")
"""La variable dependiente es el largo del cable instalado en kilmetros, y la variable independiente es el tiempo transcurrido"""
"""Donde C(h) es largo del cable instalado en kms. y h es el tiempo transcurrido en horas"""
h=6600/1.85
print(f"\n{h:.1f}\n")
def C(h):
   return 1.8*h
import matplotlib.pyplot as plt
import numpy as np
h=np.arange(0,3570,1)
plt.plot(h,C(h))
plt.title("Relacion entre el largo del cable del instalado y tiempo transcurrido")
plt.xlabel("Tiempo transcurrido (horas)")
plt.grid(True)
plt.show()

#Problema 5
print("--- Problema 5 ---")
"""Definir rango de valores del tiempo y las funciones"""
tiempo=np.arange(0,26,1)
metro=0.4*tiempo
bus=0.3*tiempo

plt.plot(tiempo, metro, label="Metro")
plt.plot(tiempo, bus, label="bus")
plt.title("Relación entre la distancia recorrida en medio de transporte y el tiempo")
plt.xlabel("Tiempo transcurrido (minutos)")
plt.ylabel("Distancia recorrida (kilometros)")
plt.grid(True)
plt.legend()
plt.show()

"""Estimar el límite superior del dominio f(t)"""
dom=round(9*1.2+8*0.5,1)
print(f"\nEl dominio contextualizado de f(t): [0; {dom}]")
k=6
m=k/0.4
b=k/0.3
print(f"El turista tardará {m}  minutos en metro y {b} minutos en bus, si la disntacia es 6km.")


print("--- Problema 6 ---")
# Definición de la función
def temperatura(t):
    return -0.5 * t**2 + 3 * t + 20

# Dominio contextualizado
t = np.arange(0,9,1)

# Valores de temperatura
T = temperatura(t)

plt.figure(figsize=(8,5))
plt.plot(t + 8, T, label="Temperatura del servidor")
plt.title("Temperatura del servidor durante la jornada laboral")
plt.xlabel("Hora del día")
plt.ylabel("Temperatura (°C)")
plt.xticks(range(8, 18))  # Marcar horas desde 8 a 17
plt.grid(True)
plt.legend()
plt.show()

# Cálculo de temperatura máxima
t_max = -3 / (2 * -0.5)
T_max = temperatura(t_max)
print(f"El servidor alcanza la temperatura máxima a las {t_max + 8:.2f} horas con {T_max:.2f} °C")

# Temperaturas a las 13:00 y 17:00 horas
t_13 = 13 - 8
t_17 = 17 - 8

T_13 = temperatura(t_13)
T_17 = temperatura(t_17)

print(f"Temperatura a las 13:00 horas: {T_13:.2f} °C")
print(f"Temperatura a las 17:00 horas: {T_17:.2f} °C")