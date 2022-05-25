print("Bem-vindo ao quiz do computador!")

playing = input("Você quer jogar? ")

if playing.lower() != "sim":
    quit()

print("Ok. Vamos jogar! ")
score = 0

answer = input("O que significa CPU? ")
if answer.lower() == "central processing unit":
    print('Correto!')
    score += 1
else:
    print("Incorreto!")

answer = input("O que significa GPU? ")
if answer.lower() == "graphics processing unit":
    print('Correto!')
    score += 1
else:
    print("Incorreto!")

answer = input("O que significa RAM? ")
if answer.lower() == "random acess memory":
    print('Correto!')
    score += 1
else:
    print("Incorreto!")

answer = input("O que significa PSU? ")
if answer.lower() == "power supply":
    print('Correto!')
    score += 1
else:
    print("Incorreto!")

print("Você acertou " + str(score) + "questões!")
print("Você acertou " + str(score / 4 * 100) + "%.")