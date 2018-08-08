# coding: utf-8
# Dígitos de Verificação do CPF
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def calcula_digitos_verificacao(cpf):
	digitos = ""
	for repeticao in range(2):
		valor = 2
		resultado = 0
		for elemento in range(len(cpf)-1, -1, -1):
			resultado += int(cpf[elemento]) * valor
			valor += 1
		digito_verificador = (10 * (resultado)) % 11

		if digito_verificador == 10:
			digitos += "0"
			cpf += "0"
		else:
			digitos += str(digito_verificador)
			cpf += str(digito_verificador)
	
	return digitos
