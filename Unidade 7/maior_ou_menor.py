# coding: utf-8
# Maiores e Menores
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

pivot = int(raw_input())
menores = []
maiores = []

while True:
	valor = int(raw_input())
	"######################"
	if valor < 0:
		break
	"######################"
	if valor <= pivot:
		menores.append(valor)
	else:
		maiores.append(valor)

print menores
print pivot
print maiores
