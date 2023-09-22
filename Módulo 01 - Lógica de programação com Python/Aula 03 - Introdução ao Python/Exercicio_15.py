"""
15. Faça um programa que receba o tamanho de um arquivo em GB e mostre o valor em:
bits
Bytes
KB
MB
"""

gigabyte = int(input("Digite o tamanho do arquivo em GB: "))
megabyte = gigabyte * 1024
kilobyte = megabyte * 1024
bytes = kilobyte * 1024
bits = bytes * 8

print(f"{gigabyte} GB é igual à {megabyte} MB, {kilobyte} KB, {bytes} Bytes e {bits} bits")
