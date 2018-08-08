# coding: utf-8
# Falta um
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def encontra_rotulo_perdido(rotulos_enviados, rotulos_recebidos):
	for i in range(len(rotulos_recebidos) - 1, -1, -1):
		for j in range(len(rotulos_enviados) - 1, -1, -1):
			if rotulos_recebidos[i] == rotulos_enviados[j]:
				rotulos_enviados.pop(j)
				
	return rotulos_enviados[0]
	
l1 = ['skol', 'brahma', 'itaipava']
l2 = ['itaipava', 'brahma']
print encontra_rotulo_perdido(l1,l2)
