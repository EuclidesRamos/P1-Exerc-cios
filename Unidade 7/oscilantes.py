# coding: utf-8
# Números Oscilantes
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

codigo = raw_input()


def verificacao(lista):
	verificador = 1
	
	for i in range(len(lista) - 1):
		if int(lista[i]) % 2 == 0 and int(lista[i + 1]) % 2 != 0:
			verificador += 1
		elif int(lista[i]) % 2 != 0 and int(lista[i + 1]) % 2 == 0:
			verificador += 1
		else:
			verificador -= 1
	
	return verificador


if verificacao(codigo) == len(codigo):
	print "verdadeiro: %d algarismos." % len(codigo)
else:
	print "falso: %d algarismos." % len(codigo)
	
