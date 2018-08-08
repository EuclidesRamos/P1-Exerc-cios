# coding: utf-8
# Sem Letras Iguais Consecutivas
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def remove_consecutivas(lista):
	
	for i in range(len(lista) - 1, -1, -1):
		tamanho = len(lista[i])
		j = 0
		while j < tamanho - 1:
			if lista[i][j].lower() == lista[i][j + 1].lower():
				lista.pop(i)
				j = tamanho
			j += 1
