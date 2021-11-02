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

def tentativa_player(): #Percorre-se a string da forca e define se o player acertou ou errou. Em caso de erro, perde-se uma vida.
    global tentativa
    tentativa = str(input()) #Se o jogador acertar, revela-se parte da palavra. Uma vez estando a palavra toda revelada, o jofador vence (vitoria == True) e fecha-se o game.
    pass #Uma pessoa pode fazer o percorrimento e a outra atrás do design do bonequinho da forca, da barra das palavras etc.

def percorrimento_palavra(guess, palavra):
    #esta função visa detectar se a letra do input esta na palavra selecionada ou não
    #função que faz a checagem pela letra na palavra

    global vidas #esta variável conta a quantidade de erros
    global posicoes_a_revelar #lista com a posição dos caracteres da palavra secreta a serem revelados
    
    if guess in palavra:
        #caso a letra esteja na palavra secreta

        print("acertou")
        
        for x in range(len(palavra)):
            #este loop percorre a palavra secreta e registra todas as posições na qual a letra adivinhada é encontrada, mesmo se houver repetições
            
            if guess == palavra[x] and x not in posicoes_a_revelar:
                #esta condicional impede que a mesma posição seja registrada várias vezes no vetor posicoes_a_revelar
                posicoes_a_revelar.append(x)
    
    else:
        #caso a letra não esteja na palavra secreta
        
        print("errou")
        
        vidas -= 1 #Diminui 1 do total de vidas
    pass

vidas = 6 #Número de tentativas. Podemos mudá-la pensando na dificuldade.
vitoria = False #Variável para vencer o jogo.
play = True #Variável para fechar o jogo, ou dar play again.
posicoes_a_revelar = [] #este vetor guarda todas as posições dos caracteres corretos

palavras = ["amar", "carro", "casa", "falar", "andar", "ovo", "bolo", "belo", "olho", "cinco",
            "especial", "teclado", "elefante", "atalho", "amarelo", "futebol", "bicicleta", "enumerar", "colaborar", "apartamento",
            "volatilidade", "axioma", "azulejo", "xilofone", "intrigante", "pizzaiolo", "endocrinologista", "escaravelho", "ampulheta", "desfibrilador"] #Palavras para usuário acertar (10 fáceis, 10 médias e 10 difíceis).
categorias = ["Gostar muito.", "Meio de transporte.", "Moradia.", "Dizer.", "Caminhar.", "Alimento.", "Alimento.", "Aquilo que tem beleza.", "Parte da cabeça.", "Numeral.",
              "Adjetivo.", "Substantivo.", "Substantivo.", "Substantivo.", "Adjetivo.", "Substantivo.", "Substantivo.", "Verbo.", "Verbo.", "Substantivo.",
              "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"] #Dicas das palavras. As palavras fáceis têm dicas bem descritivas. As médias têm dicas menos descritivas. As difíceis não têm dicas.
dificuldades = ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F",
                "M", "M", "M", "M", "M", "M", "M", "M", "M", "M",
                "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"] #Dificuldade de cada palavra, dividido em fácil (F), média (M) ou difícil (D).

while play: #Main loop do game. Eu (Rodrigo) posso fazer se preferirem.
    while vidas > 0:
        chave_aleatoria