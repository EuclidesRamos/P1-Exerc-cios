# coding: utf-8
# Turma Prática
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def decifra(chave,mensagem):
	j = 0
	mensagem_decodificada = ""
	
	while j < len(mensagem):
		for i in chave:
			if i == mensagem[j]:
				mensagem_decodificada += chave[i]
				j += 1
	
	return mensagem_decodificada
