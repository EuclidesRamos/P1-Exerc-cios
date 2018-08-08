# coding: utf-8
# Sequência Caras
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def sequencia_caras(lancamentos):
	sequencia1 = 1
	sequencia2 = 0
	caras = []
	
	for i in range(len(lancamentos)):
		if i + 1 < len(lancamentos) > 1:
			if lancamentos[i] == lancamentos[i + 1] and lancamentos[i] == 1:
				sequencia1 += 1
			elif lancamentos[i] == 1:
				sequencia2 = 1
			elif lancamentos[i] == 0 and lancamentos[i + 1] == 1:
				caras.append(sequencia1)
				sequencia1 = 1
		elif lancamentos[i] == 1:
			sequencia2 = 1
		
	caras.append(sequencia1)
	
	if len(caras) > 1:
		maior = caras[0]
		for j in range(len(caras)):
			if caras[j] > maior:
				maior = caras[j]
			elif caras[j] == maior:
				maior = caras[j]
		return maior
	elif sequencia1 >  1:
		return sequencia1
	else:
		return sequencia2
