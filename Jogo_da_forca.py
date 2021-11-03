import random 

def chave_aleatoria():
    global categoria
    global dificuldade
    global palavra
    chave = random.randrange(0, 30)
    palavra = palavras[chave]
    categoria = categorias[chave] 
    dificuldade = dificuldades[chave]
    print(f'Dica: {categoria} Dificuldade: {dificuldade}')
    pass

def tentativa_player():
    global tentativa
    tentativa = str(input("Digite uma letra: "))
    if len(tentativa) != 1:
        tentativa = "-"
    pass

def percorrimento_palavra(guess, palavra):

    global vidas
    global posicoes_a_revelar
    global jogada

    if guess in palavra:

        print("acertou")
        
        for x in range(len(palavra)):           
            if guess == palavra[x] and x not in posicoes_a_revelar:
                posicoes_a_revelar.append(x)

        for y in posicoes_a_revelar:
            jogada[y] = palavra[y]
        
        jogada = ''.join(jogada)
        
        print(jogada)

        jogada = list(jogada)
    else:
        print("errou")
        
        vidas -= 1 

    pass

def jogar_novamente():
    global play
    global start

    print("Para jogar novamente, digite 'sim'.")
    print("Para fechar o jogo, digite 'nao'.")

    play_again = str(input())

    if play_again == "sim":
        global vidas
        vidas = 6
        global posicoes_a_revelar
        posicoes_a_revelar = []
        play = True

    if play_again == "nao":
        play = False
    
    pass

vidas = 6
start = True
play = True
posicoes_a_revelar = []

palavras = ["amar", "carro", "casa", "falar", "andar", "ovo", "bolo", "belo", "olho", "cinco",
            "especial", "teclado", "elefante", "atalho", "amarelo", "futebol", "bicicleta", "enumerar", "colaborar", "apartamento",
            "volatilidade", "axioma", "azulejo", "xilofone", "intrigante", "pizzaiolo", "endocrinologista", "escaravelho", "ampulheta", "desfibrilador"]

categorias = ["Gostar muito.", "Meio de transporte.", "Moradia.", "Dizer.", "Caminhar.", "Alimento.", "Alimento.", "Aquilo que tem beleza.", "Parte da cabeça.", "Numeral.",
              "Adjetivo.", "Substantivo.", "Substantivo.", "Substantivo.", "Adjetivo.", "Substantivo.", "Substantivo.", "Verbo.", "Verbo.", "Substantivo.",
              "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

dificuldades = ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F",
                "M", "M", "M", "M", "M", "M", "M", "M", "M", "M",
                "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]

while play:
    chave_aleatoria()
    jogada = [] 

    for i in range(len(palavra)):
        jogada.append('_')
    
    while start:
        tentativa_player()

        jogada = list(jogada)
        percorrimento_palavra(tentativa, palavra)

        jogada = ''.join(jogada)       
        if jogada == palavra:
            print("Parabéns, você acertou a palavra!")
            jogar_novamente()
            break

        if vidas == 0:
            print("Que pena, você perdeu.")
            jogar_novamente()
            break