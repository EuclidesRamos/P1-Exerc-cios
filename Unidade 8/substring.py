# coding: utf-8
# Substring
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def is_substring(str1, str2):
	contador = 0
	j = 0
	
	for i in str2:
		while True:
			if j == len(str1):
				break
			if i == str1[j]:
				contador += 1
				j += 1
				break
			else:
				contador = 0
				j += 1

	if contador == len(str2):
		return True
	else:
		return False
