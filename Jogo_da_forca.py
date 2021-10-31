import random 

'''
Time, este é um esboço geral do código. Fi-lo apenas para ter uma noção. Quem não tem trecho definido pode dividir a def tentativa_player(), que é maiorzinha. 
O main loop, qualquer coisa, podemos fazer juntos.
'''
'''
Dict com as palavras e chaves numéricas (inteiras), outros dicts com infos sobre estas palavras
devem ter a mesma chave numérica. Outras infos fica a critério do Stephan, só fiz um modelo. 
'''

def chave_aleatoria(): #Gera a chave aleatória. Rodrigo fez.
    global categoria
    global dificuldade
    chave = random.randrange(30)
    palavra = palavras[chave] #Pega a palavra do dict
    categoria = categorias[chave] 
    dificuldade = dificuldades[chave]
    return palavra 

def tentativa_player(): #Percorre-se a string da forca e define se o player acertou ou errou. Em caso de errom, perde-se uma vida.
    global tentativa
    tentativa = str(input()) #Se o jogador acertar, revela-se parte da palavra. Uma vez estando a palavra toda revelada, o jofador vence (vitoria == True) e fecha-se o game.
    pass #Uma pessoa pode fazer o percorrimento e a outra atrás do design do bonequinho da forca, da barra das palavras etc.

vidas = 5 #Número de tentativas. Podemos mudá-la pensando na dificuldade.
vitoria = False #Variável para vencer o jogo.
play = True #Variável para fechar o jogo, ou dar play again.
while play: #Main loop do game. Eu (Rodrigo) posso fazer se preferirem.
    while vidas > 0:
        chave_aleatoria