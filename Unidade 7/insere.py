# coding: utf-8
# Insere Ordenado Impostor
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def insere_ordenado_impostor(lista):
	impostor = ""
	i = 0
	
	while True:
		if impostor != "":
			break
		if lista[i] > lista[i + 1]:
			impostor = lista[i + 1]
		i += 1
	
	for j in range(i - 1, - 1, -1):
		if impostor < lista[j]:
			lista[i], lista[j] = lista[j], lista[i]
			i -= 1
	
	return lista
