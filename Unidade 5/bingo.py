# coding: utf-8
# Bingo
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

cartela1 = raw_input()
cartela2 = raw_input()
bingo = 4
sorteio1 = 0
sorteio2 = 0

while sorteio1 < 4 and sorteio2 < 4:
	numero_sorteado = raw_input()
	for valor in range(len(cartela1)):
		if numero_sorteado == cartela1[valor] and numero_sorteado == cartela2[valor]:
			sorteio1 += 1
			sorteio2 += 1
		elif numero_sorteado == cartela1[valor]:
			sorteio1 += 1
		elif numero_sorteado == cartela2[valor]:
			sorteio2 += 1

if sorteio1 == sorteio2:
	print "Empate."
elif sorteio1 == 4:
	print "Bingo! Jogador 1 venceu."
else:
	print "Bingo! Jogador 2 venceu."
