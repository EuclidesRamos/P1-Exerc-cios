# coding: utf-8
# Resolve Vizinhos
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def resolve_vizinhos(lista):
	for i in range(len(lista) - 1, -1, -1):
		if i != len(lista) - 1:
			if lista[i] == lista[i - 1] == lista[i - 2]:
				lista[i - 1] += 1
				lista[i - 2] += 2
			elif lista[i] == lista[i - 1]:
				if lista[i - 1] + 1 == lista[i - 2]:
					lista[i - 1] += 2
				else:
					lista[i - 1] += 1
	return lista
