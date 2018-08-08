# coding: utf-8
# Inverte Triplas
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def inverte3a3(s):
	novo_s = ""
	sequencia_de_3 = ""
	
	for i in s:
		sequencia_de_3 += i
		if len(sequencia_de_3) == 3:
			novo_s = sequencia_de_3 + novo_s
			sequencia_de_3 = ""
	
	return novo_s
