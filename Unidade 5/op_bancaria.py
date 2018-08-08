# coding: utf-8
# Operações Bancárias
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

informacoes_do_cliente = raw_input()
cliente = informacoes_do_cliente.split()
nome_do_cliente = cliente[0]
saldo_do_cliente = float(cliente[1])
operacao = 0

while operacao < 3:
	transacao_bancaria = raw_input()
	transacao = transacao_bancaria.split()
	operacao = int(transacao[0])
	if len(transacao) == 2:
		valor = float(transacao[1])
	if operacao == 1:
		saldo_do_cliente -= valor
	elif operacao == 2:
		saldo_do_cliente += valor

print "Saldo de R$ %.2f na conta de %s" % (saldo_do_cliente, nome_do_cliente)
