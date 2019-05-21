'''
  Jogo adivinha��o
  Desenvolvido por: Matheus Maydana
'''
# Vamos utilizar a biblioteca random do python
from random import *

# Vamos setar na vari�vel numeroAleatorio um valor inteiro aleat�rio 
# entre 0 e 1000
numeroAleatorio = randint(0, 1000)

# Vamos pedir ao usu�rio o nome dele e armazenar na vari�vel nomeUsuario
nomeUsuario = input("Por favor, informe seu nome: ")
      
# Iniciamos com o while (fa�a sempre)
while True:

  # Tenta executar
  try:

	# Exibimos para o usu�rio op��es dos n�veis de jogabilidade
	# Cada valor destes correspondem a um n�vel de dificuldade
    print("[ 1 ] Izi Pizi")
    print("[ 2 ] Python")
    print("[ 3 ] Normal")
    print("[ 4 ] M�dio")
    print("[ 5 ] Dif�cil")
    print("[ 6 ] Imbass�d")
    print("[ 7 ] DEUS")
    nivelDificuldade = int(input(nomeUsuario + ", informe a dificuldade do jogo: "))

	# Depois que o usu�rio informar o n�vel de dificuldade, conseguimos delegar as tentativas para adivinhar o n�mero sorteado
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

	# Exibimos ao usu�rio a mensagem
	print('Tente adivinhar o n�mero secreto de 1 a 1000! Voc� ter� '+ str(tentativas) +' tentativas!')

	# Valor correspondente a numero X de vezes as tentativas
	indice = 0

	# Fa�a sempre que o n�mero de tentativas for maior que 0
	while tentativas > 0:
	
	   # Diminui as tentativas cada um ciclo do While
       tentativas = tentativas - 1

	   # Aumenta o �ndice, indice + 1
       indice = indice + 1;

        numeroInformado = int(input(str(a) + ': N�mero: '))
        print()
        # Se o n�mero informado for maior que o n�mero aleatorio
		
		if numeroInformado > numeroAleatorio:
		   # Exibe as mensagens
		   print('O n�mero secreto � menor!')
		   print('N�mero de tentativas: %d' % tentativas)
		   print()
		# Se o n�mero informado for menor que o n�mero aleatorio
		elif numeroInformado < numeroAleatorio:
		   # Exibe as mensagens
		   print('O n�mero secreto � maior!')
		   print('N�mero de tentativas = %d' % tentativas)
		   print()
		else:
            print('Parab�ns! Voc� acertou! O n�mero secreto �: %d' % numeroAleatorio)
            tentativas = -1
	# Se acabou as tentativas
   	if tentativas == 0:
	  # Exibe as mensagens
       print('Que pena! Voc� perdeu! Mais sorte da pr�xima vez!')
       print('O n�mero secreto era: %d' % numeroAleatorio)

	# Fim do Jogo
    elif tentativas == -1:
        input()

  # Captura falhas
  except:

    print("Ops, tente denovo!")
