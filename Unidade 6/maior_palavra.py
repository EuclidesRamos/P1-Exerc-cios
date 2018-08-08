# coding: utf-8
# Maior Palavra de Uma Frase
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def maior_palavra(frase):
	palavra_maior = ""
	palavra = ""
	
	for elemento in frase:
		if elemento != " ":
			palavra += elemento
		else:
			if len(palavra_maior) < len(palavra):
				palavra_maior = palavra
			elif len(palavra_maior) == len(palavra):
				palavra_maior = palavra
			palavra = ""
	
	if len(palavra_maior) < len(palavra):
		palavra_maior = palavra
	elif len(palavra_maior) == len(palavra):
		palavra_maior = palavra
	
	return palavra_maior
