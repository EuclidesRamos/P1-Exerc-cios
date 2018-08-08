# coding: utf-8
# Área e Volume de uma Esfera
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

import math

raio = float(raw_input())

area = 4 * math.pi * raio ** 3
volume = area / 3

print "%.2f" % volume
