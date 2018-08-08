# coding: utf-8
# Analytics Assembleia
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def conta_votos(votacao, parametro):
	contagem = []
	sim = 0
	nao = 0
	for elemento in votacao:
		entradas = elemento.split(",")
		print entradas
		if entradas[2] == str(parametro):
			if entradas[1] == "sim":
				sim += 1
			else:
				nao += 1
	contagem.append(sim)
	contagem.append(nao)
	
	return contagem
