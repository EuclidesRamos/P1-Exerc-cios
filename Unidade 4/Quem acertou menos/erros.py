# coding: utf-8
# Quem acertou menos
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

quantidade_de_entradas = int(raw_input())
alunos = []
erro = []
erros = 0 
aluno_com_mais_erros = 0
maior = 0
aluno = 1

for entrada in range(quantidade_de_entradas):
	questao = list(raw_input())
	for elemento in questao:
		if elemento == "f":
			erros = erros + 1
	alunos.append(aluno)
	erro.append(erros)
	if erros > maior:
			maior = erros
			aluno_com_mais_erros = aluno
	erros = 0
	aluno = aluno + 1


print "O aluno %d errou %d teste(s)." % (aluno_com_mais_erros, maior)
