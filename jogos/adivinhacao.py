# -*- coding: utf-8 -*-
import random as random
print("**********************************")
print(" Bem vindo ao jogo de Adivinhação ")
print("**********************************")


numero_secreto = round(random.randrange(0, 101))
print("Numero Secreto é ", numero_secreto)
total_de_tentativas = 0
pontos = 1000


print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")


nivel = int(input("Define o nível: "))
if(nivel == 1):
	total_de_tentativas = 20
elif(nivel == 2):
	total_de_tentativas = 10
else:
	total_de_tentativas = 5


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
		print("Você acertou e fez {} pontos!".format(pontos))
		break
	else:
		if(maior):
			print("Você errou! O seu numero foi maior do que o numero secreto")
		elif(menor):
			print("Você errou! O seu numero foi menor do que o numero secreto")		
		pontos_perdidos = abs(numero_secreto - chute)	
		pontos = pontos - pontos_perdidos	

print("Fim do jogo")