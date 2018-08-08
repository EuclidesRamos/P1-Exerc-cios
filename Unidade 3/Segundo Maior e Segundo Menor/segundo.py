# coding: utf-8
# Segundo Maior e Segundo Menor
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
numero4 = int(raw_input())

print "Considerando os números %d, %d, %d e %d" % (numero1, numero2, numero3, numero4)

if numero1 > numero2:
	if numero1 > numero3:
		if numero1 > numero4:
			if numero2 > numero3:
				if numero2 > numero4:
					if numero3 > numero4:
						print "O segundo menor número é", numero3
						print "O segundo maior número é", numero2
					else:
						print "O segundo menor número é", numero4
						print "O segundo maior número é", numero2
				else:
					print "O segundo menor número é", numero2
					print "O segundo maior número é", numero4
			else:
				if numero2 > numero4:
					print "O segundo menor número é", numero2
					print "O segundo maior número é", numero3
				else:
					if numero3 > numero4:
						print "O segundo menor número é", numero4
						print "O segundo maior número é", numero3
					else:
						print "O segundo menor número é", numero3
						print "O segundo maior número é", numero4
		else:
			if numero2 > numero3:
				print "O segundo menor número é", numero2
				print "O segundo maior número é", numero1
			else:
				print "O segundo menor número é", numero3
				print "O segundo maior número é", numero1
	else:
		if numero1 > numero4 and numero4 > numero2:
			print "O segundo menor número é", numero4
			print "O segundo maior número é", numero1
		elif numero1 < numero4 and numero4 < numero3:
			print "O segundo menor número é", numero1
			print "O segundo maior número é", numero4
		elif numero1 > numero4 and numero4 < numero2:
			print "O segundo menor número é", numero2
			print "O segundo maior número é", numero1
		else:
			print "O segundo menor número é", numero1
			print "O segundo maior número é", numero3
else:
	if numero2 > numero3:
		if numero2 > numero4:
			if numero1 > numero3:
				if numero1 > numero4:
					if numero3 > numero4:
						print "O segundo menor número é", numero3
						print "O segundo maior número é", numero1
					else:
						print "O segundo menor número é", numero4
						print "O segundo maior número é", numero1
				else:
					print "O segundo menor número é", numero1
					print "O segundo maior número é", numero4
			else:
				if numero1 > numero4:
					print "O segundo menor número é", numero1
					print "O segundo maior número é", numero3
				else:
					if numero3 > numero4:
						print "O segundo menor número é", numero4
						print "O segundo maior número é", numero3
					else:
						print "O segundo menor número é", numero3
						print "O segundo maior número é", numero4
		else:
			if numero1 > numero3:
				print "O segundo menor número é", numero1
				print "O segundo maior número é", numero2
			else:
				print "O segundo menor número é", numero3
				print "O segundo maior número é", numero2
	else:
		if numero2 > numero4 and numero4 > numero1:
			print "O segundo menor número é", numero4
			print "O segundo maior número é", numero2
		elif numero2 < numero4 and numero4 < numero3:
			print "O segundo menor número é", numero2
			print "O segundo maior número é", numero4
		elif numero2 > numero4 and numero4 < numero1:
			print "O segundo menor número é", numero1
			print "O segundo maior número é", numero2
		else:
			print "O segundo menor número é", numero2
			print "O segundo maior número é", numero3
