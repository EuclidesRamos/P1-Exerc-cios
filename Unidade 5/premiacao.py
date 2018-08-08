# coding: utf-8
# Premiação Cliente
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

quantidade_de_compras_joao = 0
quantidade_de_compras_julio = 0
compras_joao = 0
compras_julio = 0

while True:
	registro = raw_input().split()
	if registro[0] == "joao":
		compras_joao += float(registro[1])
		quantidade_de_compras_joao += 1
	elif registro[0] == "julio":
		compras_julio += float(registro[1])
		quantidade_de_compras_julio += 1
	else:
		break
	if quantidade_de_compras_joao > 2 or quantidade_de_compras_julio > 2:
		break
	if compras_joao >= 2000 or compras_julio >= 2000:
		break

if quantidade_de_compras_joao > 2:
		print "joao foi o vencedor. Comprou mais de duas vezes no período."
elif compras_joao > 2000:
		print "joao foi o vencedor. Comprou mais R$ 2000.00 no período."
elif quantidade_de_compras_julio > 2:
	print "julio foi o vencedor. Comprou mais de duas vezes no período."
elif compras_julio > 2000:
	print "julio foi o vencedor. Comprou mais R$ 2000.00 no período."
else:
	print "Não houve vencedor."
