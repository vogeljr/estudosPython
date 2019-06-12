# -*- coding: utf-8 -*-
def jogar():
	print("****************************")
	print(" Bem vindo ao jogo de Forca ")
	print("****************************")


	palavra_secreta  = "banana"
	letras_acertadas = ["_","_","_","_","_","_",]
	enforcou 		 = False
	acertou 		 = False

	print(letras_acertadas)

	while(not enforcou and not acertou):
		
		chute 	= input("Qual letra? ")
		chute 	= chute.strip()
		

		index = 0
		for letra in palavra_secreta:
			if(chute.upper() == letra.upper()):
				print("Encontrei a letra {} na posição {}" .format(letra, index))
				letras_acertadas[index] = letra
			index = index + 1	

	print(letras_acertadas)

if(__name__ == "__main__"):
	jogar()