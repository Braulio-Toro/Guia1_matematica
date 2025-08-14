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
