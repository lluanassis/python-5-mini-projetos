import random

vitorias_usuario = 0
vitorias_computador = 0

opcoes = ["pedra", "papel", "tesoura"]

while True:
    escolha_usuario = input("Escreva Pedra/Papel/Tesoura ou S para sair: ").lower()
    if escolha_usuario == "s":
        break

    if escolha_usuario not in opcoes:
        continue

    numero_aleatorio = random.randint(0, 2)

    escolha_computador = opcoes[numero_aleatorio]
    print("O computador escolheu", escolha_computador, ".")

    if escolha_usuario == "pedra" and escolha_computador == "tesoura":
        print("Você ganhou!")
        vitorias_usuario += 1
        continue
    elif escolha_usuario == "papel" and escolha_computador == "pedra":
        print("Você ganhou!")
        vitorias_usuario += 1
        continue
    elif escolha_usuario == "tesoura" and escolha_computador == "papel":
        print("Você ganhou!")
        vitorias_usuario += 1
        continue
    else:
        print("Você perdeu!")
        vitorias_computador += 1

print("Você ganhou", vitorias_usuario, "vezes.")
print("O computador venceu", vitorias_computador, "vezes.")
print("Tchau!")