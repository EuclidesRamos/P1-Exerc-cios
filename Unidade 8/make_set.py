# coding: utf-8
# Make Set
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def make_set(lista):
	iguais = []
	lista2 = lista
		
	for i in range(len(lista)):
		for j in range(len(lista) - 1, i, -1):
			if lista[i] == lista[j]:
				lista.pop(j)
	
	return lista
