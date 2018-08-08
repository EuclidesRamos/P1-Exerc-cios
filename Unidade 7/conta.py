# coding: utf-8
# Conta Palavras
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def conta_palavras(k, palavras):
	palavras_lista = palavras.split(":")
	maiores = 0
	
	for palavra in palavras_lista:
		if len(palavra) >= k:
			maiores += 1
			
	return maiores
