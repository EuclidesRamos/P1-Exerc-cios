# coding: utf-8
# Verifica Operações Extrato
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

limite_de_saques = int(raw_input())
saldo_da_conta = float(raw_input())

while limite_de_saques >= 0 and saldo_da_conta >= 0.00:
	transacao_bancaria = raw_input()
	transacao = transacao_bancaria.split()
	tipo = transacao[0]
	valor = float(transacao[1])
	if tipo == "saque":
		saldo_da_conta -= valor
		limite_de_saques -= 1
	elif tipo == "depósito":
		if valor <= 1000.00:
			saldo_da_conta += valor
		else:
			break

if tipo == "saque":
	saldo_da_conta += valor

print "Operação inválida: %s." % transacao_bancaria
print "Seu saldo é R$ %.2f." % saldo_da_conta
