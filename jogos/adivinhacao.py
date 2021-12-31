print("*********************************")
print("Bem-vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou", chute)

chute = int(chute)

if numero_secreto == chute:
    print("Você acertou :) ")
elif chute > numero_secreto:
        print("Você errou! O seu chute foi maior do que o número secreto. :( ")
elif chute < numero_secreto:
    print("Você errou! O seu chute foi menor do que o número secreto. :( ")

print("Fim do jogo")

