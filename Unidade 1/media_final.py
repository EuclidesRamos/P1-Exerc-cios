# coding: utf-8

n1 = float(raw_input())
n2 = float(raw_input())
n3 = float(raw_input())

p1 = float(raw_input())
p2 = float(raw_input())
p3 = 100 - (p1 + p2)

mf = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / 100

print "Média Final: %.1f" % mf
