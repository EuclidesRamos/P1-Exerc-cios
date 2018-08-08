# coding: utf-8
# Gratificação Natalina
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

codigo = int(raw_input())

if codigo == 1:
	print "Deverá receber em dezembro R$ 25000.00."
elif codigo == 2:
	print "Deverá receber em dezembro R$ 15000.00."
elif codigo == 3:
	salario = 8000.00
	faltas = int(raw_input())
	if faltas == 0:
		gratificacao = 500.00
	else:
		gratificacao = (235 - faltas) * 2.00
	print "Valor da gratificação R$ %.2f." % gratificacao
	print "Deverá receber em dezembro R$ %.2f." % (salario + gratificacao)
elif codigo == 4:
	salario = 5000.00
	faltas = int(raw_input())
	if faltas == 0:
		gratificacao = 300.00
	else:
		gratificacao = (235 - faltas) * 1.00
	print "Valor da gratificação R$ %.2f." % gratificacao
	print "Deverá receber em dezembro R$ %.2f." % (salario + gratificacao)
else:
	salario = 2800.00
	faltas = int(raw_input())
	if faltas == 0:
		gratificacao = 200.00
	else:
		gratificacao = (235 - faltas) * 0.70
	print "Valor da gratificação R$ %.2f." % gratificacao
	print "Deverá receber em dezembro R$ %.2f." % (salario + gratificacao)
