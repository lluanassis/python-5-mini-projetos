import random

alcance_maximo = input("Digite um número: ")

if alcance_maximo.isdigit():
    alcance_maximo = int(alcance_maximo)

    if alcance_maximo <= 0:
        print("Por favor, digite um número maior que 0 na próxima vez.")
        quit()
else:
    print("Por favor, digite um número próxima vez.")
    quit()

numero_aleatorio = random.randint(0, alcance_maximo)

apostas = 0

while True:
    apostas += 1
    aposta_usuario = input("Chute um número: ")
    if aposta_usuario.isdigit():
        aposta_usuario = int(aposta_usuario)
    else:
        print("Por favor, digite um número na próxima vez.")
        continue

    if aposta_usuario == numero_aleatorio:
        print("Você acertou!")
        break
    elif aposta_usuario > numero_aleatorio:
        print("Você chutou acima do número!")
    else:
        print("Você chutou abaixo do número!")

print("Você acertou", apostas, "apostas.")