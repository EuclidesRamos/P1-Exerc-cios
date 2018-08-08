# coding: utf-8
# Quantos Comeram?
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def quantos_comeram(N, fila):
	i = 0
	vendas = 0
	while True:
		if fila[i] < N:
			vendas += fila[i]
			N -= fila[i]
		elif fila[i] == N:
			vendas += N
			N -= fila[i]
			break
		elif fila[i] > N:
			break
		i += 1
	
	return vendas
