"""
20. Faça um programa que leia horas, minutos e segundos e converta para segundos.
"""

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

tempo = horas * 3600 + minutos * 60 + segundos

print(f"O tempo em segundos é {tempo}")