# coding: utf-8
# Guerra Baralho
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

jogador1 = 0
jogador2 = 0
empate = 0
carta1 = 1
carta2 = 1

while carta1 != 0 and carta2 != 0:
	carta1 = 0
	carta2 = 0
	cartas = raw_input()
	carta = cartas.split()
	carta1 = int(carta[0])
	carta2 = int(carta[1])
	if carta1 != 0 and carta2 != 0:
		if carta1 > carta2:
			jogador1 += 1
		elif carta2 > carta1:
			jogador2 += 1
		else:
			empate += 1

print "Jogador 1: %d, Jogador 2: %d, Empates: %d" % (jogador1, jogador2, empate)
