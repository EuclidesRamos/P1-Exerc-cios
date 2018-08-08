# coding: utf-8
# Conjunto com mais elementos
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

tamanhos = []
tamanho = 0


def maior_tamanho(lista):
	maior = 0
	conjunto_maior = 1
	
	for j in range(len(lista)):
		if lista[j] > maior:
			maior = lista[j]
			conjunto_maior = j + 1
			
	return conjunto_maior, maior


while True:
	numero = raw_input()

	if numero == "fim":
		break
	
	if int(numero) >= 0:
		tamanho += 1
	else:
		tamanhos.append(tamanho)
		tamanho = 0

if len(tamanhos) > 0:
	print "Conjunto %d - %d elemento(s)" % (maior_tamanho(tamanhos))
