# coding: utf-8
# Embarque Organizado
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

embarque = raw_input().split()
pares = ""
impares = ""
embarque_string = ""

for elemento in embarque:
	if int(elemento) % 2 == 0:
		pares += elemento
	else:
		impares += elemento
	embarque_string += elemento

alocacao_nova = impares + pares

if alocacao_nova == embarque_string:
	print "ok"
else:
	print "erro"
