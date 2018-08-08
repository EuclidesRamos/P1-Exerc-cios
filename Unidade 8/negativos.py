# coding: utf-8
# Negativos no fim
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def negativos_no_fim(lista):
	j = len(lista) - 1
	
	for i in range(len(lista) - 1, -1, -1):
		if lista[i] < 0:
			lista[i], lista[j] = lista[j], lista[i]
			j -= 1
