# coding: utf-8
# Soma Polinômios
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def soma_polinomios(p1, p2):
	p1_novo = p1
	p2_novo = p2
	somas = []
	
	if len(p1) > len(p2):
		for elemento in range(len(p1) - len(p2)):		
			p2_novo = [0] + p2_novo
	else:
		for elemento in range(len(p2) - len(p1)):		
			p1_novo = [0] + p1_novo

	for j in range(len(p1_novo)):
		somas.append(p1_novo[j] + p2_novo[j])
	
	return somas

