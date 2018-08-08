# coding: utf-8
# Tradutor Morse
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def tradutor_morse(mensagem):
	alfabeto_em_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	alfabeto = "abcdefghijklmnopqrstuvwxyz"
	traducao = ""

	for elemento in mensagem:		
		for i in range(len(alfabeto_em_morse)):
			if elemento == alfabeto_em_morse[i]:
				traducao += alfabeto[i]

	return traducao
