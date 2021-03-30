# encoding: utf-8

import random

#dummy (boneco)

dummy = ['''
 <<<<<<<<<<<<<<<<<<<<Hangman>>>>>>>>>>>>>>>>>>>>>
 
 +------+
 |      |
        |
        |
        | 
        |
        |
================

''', '''

 +------+
 |      |
 O      |
        |
        | 
        |
        |
================

''', '''

 +------+
 |      |
 O      |
 |      |
        | 
        |
        |
================

''', '''

  +------+
  |      |
  O      |
 /|      |
         | 
         |
         |
================

''', '''

  +------+
  |      |
  O      |
 /|\     |
         | 
         |
         |
================

''', '''

  +------+
  |      |
  O      |
 /|\     |
 /       | 
         |
         |
================

''', '''

  +------+
  |      |
  O      |
 /|\     |
 / \     | 
         |
         |
================''']


#Criando a classe Hangman (homem na forca)

class Hangman ()
    def __init__(self, word):
        self.word = word

    #metodo para adivinhar a letra
    def guess(self, letter):
        self.letter = letter

     #verifica se o jogo terminou
    def hangman_over(self):
        print('Infelizmente não foi dessa vez, tente na próxima!')

    #verifica se o jogador venceu
    def hangman_won(self):
        print('Parabéns, você conseguiu!')

    #nao mostra a letra no dummy
    def hide_word(self):

    #checa o status do game e imprime o dummy na tela
    def print_game_status(self):


#Função para ler uma palavra aleatoriamente no banco de palavras

def rand_word():
    with open("words.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
