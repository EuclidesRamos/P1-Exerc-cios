# coding: utf-8
# Remove
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def remove_divisores_k(lista, k, n):
	i = len(lista) - 1
	contador = 0
	
	while True:
		if i < 0 or contador == n:
			break
			
		if k % lista[i] == 0:
			lista.pop(i)
			contador += 1
		i -= 1
