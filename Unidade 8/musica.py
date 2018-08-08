# coding: utf-8
# Já sei tocar essa música
# (C) 2017.2, Euclides Ramos / UFCG - Programação 1

def sei_tocar_musica(musica, acordes):
	notas = 0
	j = 0

	while True:
		for i in range(len(musica)):
			for j in range(len(acordes)):
				print musica[i], notas, acordes[j]
				if musica[i] == acordes[j]:
					notas += 1
		if notas == len(musica):
			return True
		else:
			return False

musica = ["a", "d", "dm", "b"]
acordes = ["a", "d", "dm", "c", "m"]
print sei_tocar_musica(musica, acordes)

musica = ["a", "d"]
acordes = ["a", "bm", "d", "c"]
print sei_tocar_musica(musica, acordes)
