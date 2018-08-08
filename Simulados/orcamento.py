# coding: utf-8
# Orçamento Construção
# (C), 2017.2 - Euclides Ramos, UFCG - Programação 1

uni_tijolo = float(raw_input("Digite o preço da unidade do tijolo (Em reais): "))
alt_tijolo = float(raw_input("Digite a altura do tijolo (Em metros): "))
comp_tijolo = float(raw_input("Digite o comprimento do tijolo (Em metros): "))
alt_parede = float(raw_input("Digite a altura das paredes (Em metros): "))
comp_parede = float(raw_input("Digite o comprimento das paredes (Em metros): "))

num_tijolos_altura = alt_parede / alt_tijolo
num_tijolos_largura = comp_parede / comp_tijolo
num_tijolos_total = num_tijolos_altura * num_tijolos_largura
orcamento_final = num_tijolos_total * uni_tijolo

print "O número total de tijolos é %.1f e o orçamento final é de R$ %.1f" % (num_tijolos_total, orcamento_final)
