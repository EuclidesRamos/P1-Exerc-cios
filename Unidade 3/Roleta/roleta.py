# coding: utf-8
# Roleta
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

numero_aposta = int(raw_input())
cor_aposta = raw_input()
numero_sorteado = int(raw_input())
cor_sorteada = raw_input()

if numero_aposta == numero_sorteado and cor_aposta == cor_sorteada:
	pontuacao = 150
elif numero_aposta == numero_sorteado:
	pontuacao = 100
elif cor_aposta == cor_sorteada:
	pontuacao = 50
	if numero_sorteado > numero_aposta:
		pontuacao = pontuacao + 30
	else:
		pontuacao = pontuacao + 50
else:
	pontuacao = 0

print pontuacao
