# coding: utf-8
# Troca Chave
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def troca_chave(dic):
	novo_dic = {}
	
	for i in dic:
		novo_dic[dic[i]] = i
	return novo_dic
