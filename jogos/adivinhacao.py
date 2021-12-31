print("*********************************")
print("Bem-vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
total_radada = total_de_tentativas

while total_de_tentativas > 0:

    print("Tentativa", rodada, "de", total_radada)
    chute = input("Digite o seu número: ")
    print("Você digitou", chute)
    chute = int(chute)

    if numero_secreto == chute:
        print("Você acertou :) ")
        break
    elif chute > numero_secreto:
            print("Você errou! O seu chute foi maior do que o número secreto. :( ")
            total_de_tentativas = total_de_tentativas - 1
    elif chute < numero_secreto:
        print("Você errou! O seu chute foi menor do que o número secreto. :( ")
        total_de_tentativas = total_de_tentativas - 1

    rodada = rodada + 1

print("Fim do jogo")

