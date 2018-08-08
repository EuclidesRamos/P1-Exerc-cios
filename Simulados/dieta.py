# coding: utf-8
# Dias de Dieta
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

peso = float(raw_input())
tempo = float(raw_input())
cal_consumida = float(raw_input())

peso_cal = peso * 7700
tempo_cal = tempo * 900
quant_dias = peso_cal / (tempo_cal + 2000 - cal_consumida)

print "Você precisará de %.2f dias de dieta" % quant_dias
