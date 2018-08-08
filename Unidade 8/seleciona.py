# coding: utf-8
# Filtra Divisores
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def filtra_divisores(lista):
	soma = 0
	j = 0
	
	for i in range(len(lista) - 1, -1, -1):
		numero = str(lista[i])
		while j < len(numero):
			soma += int(numero[j])
			j += 1
		if lista[i] % soma != 0:
			lista.pop(i)
		soma = 0
		j = 0
