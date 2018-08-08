# coding: utf-8
# Quantos Comeram?
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def cesar(msg, d):
	alfabeto = "abcdefghijklmnopqrstuvwxyz"
	mensagem_criptografada = ""

	for elemento in msg:
		teste = 0
		for i in range(len(alfabeto)):
			if elemento == alfabeto[i]:
				teste = 1
				if i + d < len(alfabeto) - 1:
					mensagem_criptografada += alfabeto[i + d]
				else:
					mensagem_criptografada += alfabeto[i + d - len(alfabeto)]
		if teste == 0:
			mensagem_criptografada += elemento

	return mensagem_criptografada
