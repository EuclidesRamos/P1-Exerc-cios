# coding: utf-8
# Resumo das Vendas
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

total = int(raw_input())
vendas_teresa = int(raw_input())
vendas_carla = int(raw_input())

vendas_joaquim = total - vendas_teresa - vendas_carla
porcentagem_teresa = vendas_teresa * 100.0 / total
porcentagem_joaquim = vendas_joaquim * 100.0 / total
porcentagem_carla = vendas_carla * 100.0 / total

print "Teresa vendeu %d (de %d) brinquedos. (%.2f%%)" % (vendas_teresa, total, porcentagem_teresa)
print "Joaquim vendeu %d (de %d) brinquedos. (%.2f%%)" % (vendas_joaquim, total, porcentagem_joaquim)
print "Carla vendeu %d (de %d) brinquedos. (%.2f%%)" % (vendas_carla, total, porcentagem_carla)
