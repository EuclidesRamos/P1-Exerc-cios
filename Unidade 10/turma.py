# coding: utf-8
# Turma Prática
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def turma_pratica(alocacao, t):
	alunos_matriculados = 0
	
	for i in alocacao:
		if alocacao[i][1] == t:
			alunos_matriculados += 1
	
	return alunos_matriculados
