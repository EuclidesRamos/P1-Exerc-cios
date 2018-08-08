# coding: utf-8
# Operações Bancárias
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

razao = int(raw_input())
pa = ""
numeros = []
numero = ""
seguinte = 1
eh_pa = 1
pas = 0

while pa != "fim":
	pa = raw_input()
	if pa != "fim":
		for elemento in pa:
			if elemento != " ":
				numero += elemento
			else:
				numeros.append(numero)
				numero = ""
		numeros.append(numero)
		numero = ""
		for valor in range(len(numeros)):
			if valor != len(numeros) - 1:
				if int(numeros[valor]) + razao == int(numeros[seguinte]):
					eh_pa += 1
					seguinte += 1
		if eh_pa == len(numeros):
			pas += 1
		numeros = []
		seguinte = 1
		eh_pa = 1

print pas
