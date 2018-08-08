# coding: utf-8
# Elimina Menores
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def elimina_menores(num, lista):
	removidos = 0
	
	for i in range(len(lista) - 1, -1, -1):
		if lista[i] < num:
			lista.pop(i)
			removidos += 1
	
	return removidos
