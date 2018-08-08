# coding: utf-8
# Classifica Corredor
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

km_percorrido = float(raw_input())
tempo = float(raw_input())

km_por_hora = km_percorrido / tempo

if km_por_hora < 10.0:
	print "Velocidade: %.1fkm/h. Corredor amador." % km_por_hora
elif km_por_hora > 15.0:
	print "Velocidade: %.1fkm/h. Corredor profissional." % km_por_hora
else:
	print "Velocidade: %.1fkm/h. Corredor aspirante." % km_por_hora
