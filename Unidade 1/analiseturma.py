# coding: utf-8
# Percentagem de aprovados
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

print "Análise da Turma"
print "==="
alunos_aprovados = int(raw_input("Número de aprovados? "))
alunos_reprovados = int(raw_input("Número de reprovados? "))

total_de_alunos = alunos_aprovados + alunos_reprovados
percentagem_de_aprovados = (alunos_aprovados * 100.0) / total_de_alunos
percentagem_de_reprovados = (alunos_reprovados * 100.0) / total_de_alunos

print "---"
print "Total de alunos na turma: %d" % total_de_alunos
print "Aprovados: %d = %.1f%%" % (alunos_aprovados, percentagem_de_aprovados)
print "Reprovados: %d = %.1f%%" % (alunos_reprovados, percentagem_de_reprovados)
