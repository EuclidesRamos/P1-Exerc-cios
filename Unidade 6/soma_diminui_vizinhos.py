# coding: utf-8
# Soma e Dimunui Vizinhos!
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def soma_diminui_vizinhos(lista):
	soma = 1
	dimunui = 2
	resultado = 0
	for elemento in range(len(lista)):
		if elemento == 0:
			resultado = resultado + lista[elemento]
		elif elemento % 2 != 0:
			resultado = resultado + lista[elemento]
		elif elemento % 2 == 0:
			resultado = resultado - lista[elemento]
		if len(lista) == 0:
			resultado = 0
	return resultado
