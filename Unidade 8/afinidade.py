# coding: utf-8
# Afinidade Musical
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def tem_afinidade(l1, l2):
	iguais = 0
	
	for i in l1:
		for j in l2:
			if i == j:
				iguais += 1
	
	if iguais >= 3:
		return True
	else:
		return False
