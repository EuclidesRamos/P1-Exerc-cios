# coding: utf-8
# Agenda Telefônica
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

# Organiza os elementos da agenda em ordem alfabética
def ordena_agenda(lista):
	for valor in range(len(lista) - 1):
		for contato in range(len(lista) - 1 - valor):
			if lista[contato][0] > lista[contato + 1][0]:
				lista[contato], lista[contato + 1] = lista[contato + 1], lista[contato]

# Realiza a busca do elemento na agenda
def busca_elemento(elemento, lista):
	teste = 0
	for contato in lista:
		if contato[0] == elemento:
			teste = 1
			print "Nome: %s" % contato[0]
			print "Fone: %s" % contato[1]
			print "----------"
		
	if teste == 0:
		print "Nome inexistente"
		print "----------"

# Imprime todos os contatos da Agenda
def imprime_agenda(lista):
	for contato in lista:
		print "Nome: %s" % contato[0]
		print "Fone: %s" % contato[1]
		print "----------"

agenda = []

while True:
	operacao = raw_input()
	if operacao == "finalizar":
		break
	if operacao == "inserir":
		insercoes = int(raw_input())
		for i in range(insercoes):
			nome = raw_input()
			numero = raw_input()
			agenda.append((nome,numero))
			ordena_agenda(agenda)
	elif operacao == "buscar":
		busca = raw_input()
		busca_elemento(busca, agenda)
	elif operacao == "imprimir":
		imprime_agenda(agenda)
