import random

def imprime_mensagem_abertura():

    print("*********************************")
    print("***Bem vindo no jogo de forca!***")
    print("*********************************")


def carrega_palavra_secreta():

    arquivo = open("palavras.txt", "r", encoding="UTF-8")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()

    return palavras[random.randrange(0, len(palavras))]

def iniciliza_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra ? ")
    return chute.strip().upper()


def jogar_forca():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = iniciliza_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra

                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou !")
    else:
        print("Você perdeu !")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar_forca()
