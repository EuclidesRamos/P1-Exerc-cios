# coding: utf-8
# Tiro ao Alvo
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

import math
distancias = []
distancia = 0
disparos = 0
media = 0

while distancia <= 200:
	coordenadas = raw_input().split(",")
	distancia = math.sqrt(float(coordenadas[0]) ** 2 + float(coordenadas[1]) ** 2)
	if distancia <= 200:
		distancias.append(distancia)
		disparos += 1

for valor in distancias:
	media += valor
	print "%.2f" % valor 

print "--"
print "num disparos: %d" % disparos
if disparos != 0:
	print "distancia media: %.2f" % (media / len(distancias))
else:
	print "distancia media: 0.00"
