# coding: utf-8
# Um Passo do Algoritmo BubbleSort
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

nova_sequencia = ""

# Faz split da entrada
def meu_split(string):
	sequencia_lista = []
	numero = ""
	
	for i in string:
		if i != " ":
			numero += i
		else:
			sequencia_lista.append(int(numero))
			numero = ""
	sequencia_lista.append(int(numero))
	
	return sequencia_lista
	
# Faz o primeiro passo da ordenação BubbleSort
def ordenando_lista(lista):
	
	for i in range(len(lista) - 1):
			if int(lista[i]) > int(lista[i + 1]):
				lista[i], lista[i + 1] = lista[i + 1], lista[i]
	
	return lista



while True:
	sequencia = raw_input()

	if sequencia == "fim":
		break

	else:
		sequencia = meu_split(sequencia)
		ordenando_lista(sequencia)
		for elemento in sequencia:
			if elemento != sequencia[len(sequencia) - 1]:
				nova_sequencia += str(elemento) + " "
			else:
				nova_sequencia += str(elemento)
		
		print nova_sequencia
		nova_sequencia = ""
