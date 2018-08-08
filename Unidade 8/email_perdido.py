# coding: utf-8
# Email Perdido
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def encontra_email_perdido(emails_enviados, emails_recebidos):
	for i in range(len(emails_recebidos) - 1, -1, -1):
		for j in range(len(emails_enviados) - 1, -1, -1):
			if emails_recebidos[i] == emails_enviados[j]:
				emails_enviados.pop(j)
				
	return emails_enviados[0]
