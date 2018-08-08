# coding: utf-8
# Questoes para mt
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def seleciona_questoes(todas, utilizadas):
	for i in range(len(utilizadas) - 1, -1, -1):
		for j in range(len(todas) - 1, -1, -1):
			if utilizadas[i] == todas[j]:
				todas.pop(j)
