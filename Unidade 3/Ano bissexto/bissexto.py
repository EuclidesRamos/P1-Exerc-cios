# coding: utf-8
# Ano Bissexto
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

ano = int(raw_input())

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
	print "%d é bissexto" % ano
else:
	print "%d não é bissexto" % ano
