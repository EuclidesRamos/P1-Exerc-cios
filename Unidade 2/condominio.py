# coding: utf-8
# Condomínio
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

lado1 = float(raw_input())
lado2 = float(raw_input())
area_da_casa = float(raw_input())

area_do_terreno = lado1 * lado2
quantidade_de_casas = int(area_do_terreno / area_da_casa)

print "%d casa(s) pode(m) ser construída(s) no terreno." % quantidade_de_casas
