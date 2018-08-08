# coding: utf-8
# Squeeze
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def squeeze(lista):
	i = len(lista) - 1
	
	while i > 0:
		if lista[i] == lista[i - 1]:
			lista.pop(i)
		i -= 1
	
	return lista
