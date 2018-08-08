# coding: utf-8
# Subtração de Polinomios
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def subtrai_polinomios(p1, p2):
	i = 0
	j = 0
	resultado = []
	
	while True:
		if i == len(p1):
			subtracao = 0 - p2[j]
			resultado.append(subtracao)
			j += 1
		elif j == len(p2):
			resultado.append(p1[i])
			i += 1
		else:
			subtracao = p1[i] - p2[j]
			if p1[i] == 0 and p2[j] == 0:
				resultado.append(0)
			elif subtracao != 0:
				resultado.append(subtracao)
			i += 1
			j += 1
		
		if i == len(p1) and j == len(p2):
			return resultado
