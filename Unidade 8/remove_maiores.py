# coding: utf-8
# Remove Maiores
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def remove_maiores(lista):
	maior = 0
	
	for i in lista:
		if i > maior:
			maior = i
	for i in range(len(lista) - 1, -1, -1):
		if maior == lista[i]:
			lista.pop(i)
