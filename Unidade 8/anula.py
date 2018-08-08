# coding: utf-8
# Remove Números Opostos Adjacentes
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def anula(lista):
	i = 0
	
	while i < len(lista) - 1:
		if lista[i] + lista[i + 1] == 0:
			lista.pop(i + 1)
			lista.pop(i)
			i = -1
		i += 1
