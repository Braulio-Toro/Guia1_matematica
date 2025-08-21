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
print(f"{h:.1f}")
def C(h):
   return 1.8*h
import matplotlib.pyplot as plt
import numpy as np
h=np.arange(0,3570,1)
plt.plot(h,C(h))
plt.tittle("Relacion entre el largo del cable del instalado y tiempo transcurrido")
plt.xlabel("Tiempo transcurrido (horas)")
plt.grid(True)
plt.show()
