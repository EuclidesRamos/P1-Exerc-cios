# coding: utf-8
# Iniciadas por consoantes
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

numero_de_palavras = int(raw_input())
iniciais = []
consoantes = 0
for quantidade in range(0, numero_de_palavras):
	palavra = raw_input().lower()
	iniciais.append(palavra[0])

for letra in iniciais:
	if "a" != letra and "e" != letra and "i" != letra and "o" != letra and "u" != letra:
		consoantes = consoantes + 1

porcentagem = consoantes * 100.0 / numero_de_palavras
print "total de palavras: %d" % numero_de_palavras
print "iniciadas por consoantes: %d (%.2f%%)" % (consoantes, porcentagem)
