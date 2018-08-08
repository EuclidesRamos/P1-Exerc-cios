# coding: utf-8
# Altera Vetor
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def altera_vetor_por_escalar(vetor, escalar):
	for i in range(len(vetor)):
		vetor[i] *= escalar
