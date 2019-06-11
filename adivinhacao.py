# -*- coding: utf-8 -*-
print("**********************************")
print(" Bem vindo ao jogo de Adivinhação ")
print("**********************************")
import random as random

numero_secreto = round(random.randrange(0, 101))
print("Numero Secreto é ", numero_secreto)
total_de_tentativas = 3
rodada = 1


for rodada in range(1, total_de_tentativas + 1):
	print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
	chute_str = input("Digite um número entre 1 e 100: ")
	# print("Você digitou ", chute_str)
	# print(type(chute_str)) # verificando tipo da variavel
	chute = int(chute_str) # convertendo str p/ int

	if(chute < 1 or chute >100):
		print("VC deve digitar uma número entre 1 a 100")
		continue

	acertou = numero_secreto == chute
	maior   = chute > numero_secreto
	menor   = chute < numero_secreto

	if (acertou):
		print("Você acertou!")
		break
	else:
		if(maior):
			print("Você errou! O seu numero foi maior do que o numero secreto")
		elif(menor):
			print("Você errou! O seu numero foi menor do que o numero secreto")		

print("Fim do jogo")