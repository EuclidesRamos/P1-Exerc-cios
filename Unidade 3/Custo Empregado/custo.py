# coding: utf-8
# Custo Empregado
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

salario_base = float(raw_input())
dias_trabalhados = int(raw_input())
custo_transporte = float(raw_input())

custo_transporte_total = custo_transporte * dias_trabalhados
custo_maximo_transporte = salario_base * 0.06
fgts_empregador = salario_base * 0.08
inss_empregador = salario_base * 0.12

if salario_base <= 1317.07:
	inss_empregado = salario_base * 0.08
elif salario_base > 2195.12:
	inss_empregado = salario_base * 0.11
else:
	inss_empregado = salario_base * 0.09 

if custo_transporte_total > custo_maximo_transporte:
	gasto_empregado = custo_maximo_transporte
	gasto_empregador = custo_transporte_total - custo_maximo_transporte
else:
	gasto_empregado = 0
	gasto_empregador = 0

custo_empregador = gasto_empregador + fgts_empregador + \
	inss_empregador + salario_base
salario_liquido = salario_base - inss_empregado - gasto_empregado

print "O salário base é R$ %.2f" % salario_base
print "O custo mensal para o empregador é de R$ %.2f" % custo_empregador
print "O salário líquido que o trabalhador irá receber no mês é R$ \
%.2f" % salario_liquido
