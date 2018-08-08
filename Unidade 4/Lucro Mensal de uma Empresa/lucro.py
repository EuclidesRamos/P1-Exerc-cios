# coding: utf-8
# Lucro Mensal de uma Empresa
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

receita = []
despesas = []
lucro_total = []
for local in range(0, 12):
	valor = raw_input()
	numero = valor.split()
	receita.append(numero[0])
	despesas.append(numero[1])
	lucro = (float(receita[local]) - float(despesas[local]))
	lucro_total.append(lucro)

meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
valor = 0
for mes in meses:
	print "%s %4.1f" % (mes, lucro_total[valor])
	valor = valor + 1
