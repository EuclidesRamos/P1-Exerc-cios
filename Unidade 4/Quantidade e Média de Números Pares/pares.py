# coding: utf-8
# Quantidade e Média de Números Pares
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

numeros_lidos = int(raw_input())
soma = 0
contador = 0.0
numeros = []
numeros_abaixo_da_media = 0

for valor in range(0, numeros_lidos):
	numero = int(raw_input())
	numeros.append(numero)
	if numero % 2 == 0:
		soma = soma + numero
		contador = contador + 1

media = soma / contador

for valor in numeros:
	if valor < media:
		numeros_abaixo_da_media = numeros_abaixo_da_media + 1
		
print "soma: %d" % soma
print "média: %.1f" % media
print "%d número(s) abaixo da média" % numeros_abaixo_da_media
