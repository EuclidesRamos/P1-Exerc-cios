# coding: utf-8
# Imprime Nota Fiscal
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

valor_total = float(raw_input())
data = raw_input()
quantidade_de_produtos = int(raw_input())

media = float(valor_total / quantidade_de_produtos)
print "Data: %s" % data
print "O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f." % (valor_total, media)
