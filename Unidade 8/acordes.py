# coding: utf-8
# Acordes aprendidos
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def meu_in(elemento, lista):
	for i in lista:
		if elemento == i:
			return True
	
	return False

def acordes(musica_1, musica_2):
	i = 0
	j = 0
	acordes = []
	
	while i < len(musica_1) or j < len(musica_2):
		if i == len(musica_1):
			if meu_in(musica_2[j], musica_1) == False:
				acordes.append(musica_2[j])
			j += 1
		elif j == len(musica_2):
			acordes.append(musica_1[i])
			i += 1		
		elif meu_in(musica_2[j], musica_1) == True:
			acordes.append(musica_1[i])
			i += 1
		elif meu_in(musica_2[j], musica_1) == False:
			acordes.append(musica_1[i])
			i += 1
		
	return acordes
