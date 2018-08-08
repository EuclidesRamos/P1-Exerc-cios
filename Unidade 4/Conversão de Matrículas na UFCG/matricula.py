# coding: utf-8
# Conversão de Matrículas na UFCG
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

matricula_antiga = raw_input()
matricula = ""

for elemento in range(len(matricula_antiga)):
	
	if elemento == 0: 
		matricula = matricula + "1"
	elif elemento == 4:
		matricula = matricula + matricula_antiga[elemento] + "0"
	else:
		matricula = matricula + matricula_antiga[elemento]

print matricula
