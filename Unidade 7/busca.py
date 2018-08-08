# coding: utf-8
# Busca Linear
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def busca(sequencia, valor):
	i = 0
	
	while True:
		if i > len(sequencia) - 1:
			return -1
		elif sequencia[i] == valor:
			return i
		i += 1
