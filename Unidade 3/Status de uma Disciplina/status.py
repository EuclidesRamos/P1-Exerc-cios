# coding: utf-8
# Status de uma Disciplina
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
faltas = int(raw_input())

media = (nota1 + nota2 + nota3) / 3
porcentagem_de_faltas = faltas * 100 / 30

if porcentagem_de_faltas <= 25 and media >= 7.0:
	print "aprovado por media"
elif porcentagem_de_faltas > 25:
	print "reprovado por faltas"
elif media < 4.0:
	print "reprovado por nota"
else:
	print "prova final"
