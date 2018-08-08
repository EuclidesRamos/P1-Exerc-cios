# coding: utf-8
# Controle de Água
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

import math

velocidade_de_vasao = float(raw_input())                 #Em metros/segundo
diametro_do_cano = float(raw_input())                    #Em metros
tempo = int(raw_input())                                 #Em segundos

seccao = (math.pi * diametro_do_cano ** 2) / 4
vazao = velocidade_de_vasao * seccao * 1000
quantidade_de_agua = tempo * vazao

print "Quantidade de água =", quantidade_de_agua, "litros."
