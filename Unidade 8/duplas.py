# coding: utf-8
# Duplas do Projeto
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def meu_in(lista, elemento):
	teste = 0
	for i in lista:
		if i == elemento:
			teste = 1
	if teste == 1:
		return True
	else:
		return False

def insere_nome(aluno1, duplas, aluno2):
	duplas.append(aluno1)
	i = len(duplas) - 2
	j = len(duplas) - 1
	
	while True:
		if i < 0 or meu_in(duplas, aluno2) == False:
			break
		if duplas[i] != aluno2:
			duplas[i], duplas[j] = duplas[j], duplas[i]
			j -= 1
			i -= 1
		elif duplas[i] == aluno2:
			duplas[i], duplas[j] = duplas[j], duplas[i]
			break
