# coding: utf-8
# Nota na Final
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

print "== Estágio 1 =="
peso_a = float(raw_input("Peso? "))
nota_a = float(raw_input("Nota? "))

print "== Estágio 2 =="
peso_b = float(raw_input("Peso? "))
nota_b = float(raw_input("Nota? "))

print "== Estágio 3 =="
peso_c = float(raw_input("Peso? "))
nota_c = float(raw_input("Nota? "))

media_parcial = (nota_a * peso_a) + (nota_b * peso_b) + (nota_c * peso_c)
nota_pra_media_5 = (5.0 - (media_parcial * 0.6)) / 0.4
nota_pra_media_7 = (7.0 - (media_parcial * 0.6)) / 0.4

print "== Resultados =="
print "Média parcial:", media_parcial
print "Nota na final, pra média 5.0 = %.1f" % nota_pra_media_5
print "Nota na final, pra média 7.0 = %.1f" % nota_pra_media_7
