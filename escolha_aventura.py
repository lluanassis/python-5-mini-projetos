nome = input("Escreva o seu nome: ")
print("Bem vindo", nome, "a essa aventura!")

resposta = input("Você está em uma estrada sombria e frente a uma bifurcação. Escolha a qual lado seguir (direita/esquerda). ").lower()

if resposta == "esquerda":
    resposta = input(
        "Você chegou no rio, vai escolher circundar à pé ou nadar (andar/nadar)? ")
    if resposta == "nadar":
        print("Você nadou no rio e foi comido por um jacaré.")
    elif resposta == "andar":
        print("Você andou muitos quilômetros, correu da água e se perdeu.")
    else:
        print("Opção inválida. Fim de jogo.")


elif resposta == "direita":
    resposta = input("Você chegou na ponte, ela parece insegura, você prefere atravessá-la ou voltar o caminho (atravessar/voltar)?")

    if resposta == "voltar":
        print("Você voltou e perdeu.")
    elif resposta == "atravessar":
        resposta = input("Você atravessa a ponte e conhece um estranho. Você quer falar com ele (sim/não)?")

        if resposta == "sim":
            print ("Você falou com um estranho e ele o presenteou com ouro. Você venceu!")
        elif resposta == "não":
            print("Você ignorou o estranho, ele se ofendeu e o matou. Você perdeu.")
        else: print("Opção inválida. Você perdeu.")
else:
    print("Opção inválida. Você perdeu.")

print("Obrigado pela tentativa", nome)