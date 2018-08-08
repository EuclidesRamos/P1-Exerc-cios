a = float(raw_input("Medida do Cateto 1? "))
b = float(raw_input("Medida do Cateto 2? "))

from math import sqrt

h = sqrt((a ** 2) + (b ** 2))

print "Medida da Hipotenusa: %.2f" % h
