'''
  Jogo adivinhação
  Desenvolvido por: Matheus Maydana
'''
# Vamos utilizar a biblioteca random do python
from random import *

# Vamos setar na variável numeroAleatorio um valor inteiro aleatório 
# entre 0 e 1000
numeroAleatorio = randint(0, 1000)

# Vamos pedir ao usuário o nome dele e armazenar na variável nomeUsuario
nomeUsuario = input("Por favor, informe seu nome: ")
      
# Iniciamos com o while (faça sempre)
while True:

  # Tenta executar
  try:

	# Exibimos para o usuário opções dos níveis de jogabilidade
	# Cada valor destes correspondem a um nível de dificuldade
    print("[ 1 ] Izi Pizi")
    print("[ 2 ] Python")
    print("[ 3 ] Normal")
    print("[ 4 ] Médio")
    print("[ 5 ] Difícil")
    print("[ 6 ] Imbasséd")
    print("[ 7 ] DEUS")
    nivelDificuldade = int(input(nomeUsuario + ", informe a dificuldade do jogo: "))

	# Depois que o usuário informar o nível de dificuldade, conseguimos delegar as tentativas para adivinhar o número sorteado
    tentativas = 1
    if nivelDificuldade == 1:
      tentativas = 25
    elif nivelDificuldade == 2:
      tentativas = 20
    elif nivelDificuldade == 3:
      tentativas = 15
    elif nivelDificuldade == 4:
      tentativas = 10
    elif nivelDificuldade == 5:
      tentativas = 7
    elif nivelDificuldade == 6:
      tentativas = 4

	# Exibimos ao usuário a mensagem
	print('Tente adivinhar o número secreto de 1 a 1000! Você terá '+ str(tentativas) +' tentativas!')

	# Valor correspondente a numero X de vezes as tentativas
	indice = 0

	# Faça sempre que o número de tentativas for maior que 0
	while tentativas > 0:
	
	   # Diminui as tentativas cada um ciclo do While
       tentativas = tentativas - 1

	   # Aumenta o índice, indice + 1
       indice = indice + 1;

        numeroInformado = int(input(str(a) + ': Número: '))
        print()
        # Se o número informado for maior que o número aleatorio
		
		if numeroInformado > numeroAleatorio:
		   # Exibe as mensagens
		   print('O número secreto é menor!')
		   print('Número de tentativas: %d' % tentativas)
		   print()
		# Se o número informado for menor que o número aleatorio
		elif numeroInformado < numeroAleatorio:
		   # Exibe as mensagens
		   print('O número secreto é maior!')
		   print('Número de tentativas = %d' % tentativas)
		   print()
		else:
            print('Parabéns! Você acertou! O número secreto é: %d' % numeroAleatorio)
            tentativas = -1
	# Se acabou as tentativas
   	if tentativas == 0:
	  # Exibe as mensagens
       print('Que pena! Você perdeu! Mais sorte da próxima vez!')
       print('O número secreto era: %d' % numeroAleatorio)

	# Fim do Jogo
    elif tentativas == -1:
        input()

  # Captura falhas
  except:

    print("Ops, tente denovo!")
