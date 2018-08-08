# coding: utf-8
# Único
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def unico(string):
	string_nova = ""
	
	for elemento in range(len(string)):
		if len(string) - 1 != elemento != 0:
			if string[elemento] == string[elemento - 1] and string[elemento] != string[elemento + 1]:
				string_nova += string[elemento]
			elif string[elemento] != string[elemento - 1] and string[elemento] != string[elemento + 1]:
				string_nova += string[elemento]
		elif elemento == 0:
			if string[elemento] != string[elemento + 1]:
				string_nova += string[elemento]
		elif elemento == len(string) - 1:
			string_nova += string[elemento]
	
	return string_nova
