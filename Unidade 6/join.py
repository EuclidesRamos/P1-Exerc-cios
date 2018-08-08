# coding: utf-8
# Minha Implementação para o método join
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def meu_join(delimitador, sequencia_de_string):
	nova_sequencia = ""
	for i in range(len(sequencia_de_string)):
		if i > 0:
			nova_sequencia += delimitador + sequencia_de_string[i]
		else:
			nova_sequencia += sequencia_de_string[i]
	return nova_sequencia
