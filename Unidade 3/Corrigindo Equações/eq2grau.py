# coding: utf-8
# Corrigindo Equações
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

import math
delta = b ** 2 - 4 * a * c

if delta < 0:
	print "sem raizes reais"
elif delta == 0:
	x = (- b + math.sqrt(delta)) / (2.0 * a)
	print "x = %.2f" % x
else:
	x1 = (- b + math.sqrt(delta)) / (2.0 * a)
	x2 = (- b - math.sqrt(delta)) / (2.0 * a)
	print "x1 = %.2f" % x1
	print "x2 = %.2f" % x2
