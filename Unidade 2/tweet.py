# coding: utf-8
# Tweets por Página
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

quantidade_de_tweets = int(raw_input())

tweets_perdidos = float(quantidade_de_tweets % 400)
porcentagem = (tweets_perdidos * 100) / quantidade_de_tweets
quantidade_de_paginas = quantidade_de_tweets / 400
simbolo = "%"

print "Serão necessárias %d página(s) para visualizar os tweets." % quantidade_de_paginas
print "%.1f%s dos tweets serão perdidos." % (porcentagem, simbolo)
