# coding: utf-8
# Soma Intervalo
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def soma_intervalo(a,b):
	soma = 0
	for numero in range(a,b+1):
		soma += numero
	
	return soma
