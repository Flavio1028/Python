import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo********")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo ?"))

if jogo == 1:
    forca.jogar_forca()
elif jogo == 2:
    adivinhacao.jogar_adivinhacao()
else:
    print("Opção inválida")

