# coding: utf-8
# Avaliação Docente
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

quantidade_semestres = int(raw_input())
ensino = int(raw_input())
intelectual = int(raw_input())
orientacao = int(raw_input())
administrativa = int(raw_input())

media_pontos = (ensino + intelectual + orientacao + administrativa) / 4
ensino_minima = bool(ensino >= 320)
intelectual_minima = bool(intelectual >= 100)
orientacao_minima = bool(orientacao >= 20)

if quantidade_semestres >= 4:
	if ensino_minima and intelectual_minima and orientacao_minima is True:
		if media_pontos >= 140:
			print "Promoção deferida. Parabéns!"
		else:
			print "Promoção indeferida. Média insuficiente."
	else:
		print "Promoção indeferida. Pontuação mínima não alcançada."
else:
	print "Promoção indeferida. Número de semestres insuficiente."
