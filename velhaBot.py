import os
import random

colun1 = "1 / 2 / 3"
colun2 = "4 / 5 / 6"
colun3 = "7 / 8 / 9"

bot = 1
marcacao = ""
alternancia = 1

def printTabela():
    print("==================")
    print("Jogo da Velha")
    print(colun1)
    print(colun2)
    print(colun3)
    print("Digite o número da posição para marcar, e 0 para sair.")
    print("==================")

def mensagemVitoria():
    if (alternancia % 2 == 0):
        print("Que pena! Você perdeu!")
        os._exit(checaVitoria == True)
    else:
        print("Você venceu!") 
        os._exit(checaVitoria == True) 

def checaVitoria():
    if colun1 == "x / x / x" or colun1 == "o / o / o":
        mensagemVitoria()
    if colun2 == "x / x / x" or colun2 == "o / o / o":
        mensagemVitoria()        
    if colun3 == "x / x / x" or colun3 == "o / o / o":
        mensagemVitoria()
    if colun1[0] == "x" and colun2[0] == "x" and colun3[0] == "x" or colun1[0] == "o" and colun2[0] == "o" and colun3[0] == "o":
        mensagemVitoria()
    if colun1[4] == "x" and colun2[4] == "x" and colun3[4] == "x" or colun1[4] == "o" and colun2[4] == "o" and colun3[4] == "o":
        mensagemVitoria()                     
    if colun1[8] == "x" and colun2[8] == "x" and colun3[8] == "x" or colun1[8] == "o" and colun2[8] == "o" and colun3[8] == "o":
        mensagemVitoria()                    
    if colun1[0] == "x" and colun2[4] == "x" and colun3[8] == "x" or colun1[0] == "o" and colun2[4] == "o" and colun3[8] == "o":
        mensagemVitoria()
    if colun1[8] == "x" and colun2[4] == "x" and colun3[0] == "x" or colun1[8] == "o" and colun2[4] == "o" and colun3[0] == "o":
        mensagemVitoria()
    if alternancia == 10:
        print("Deu velha!")
        os._exit(1 == 1)
 

os.system('cls')
printTabela()

while True:
    if (alternancia % 2 == 0):
        resposta = int(input("Aonde você deseja marcar?" ))
        marcacao = "o"
    else:
        bot = random.randint(1, 9) 
        resposta = bot
        marcacao = "x"

    if resposta == 1:
        os.system('cls')   
        if colun1[0] == "1":
            colun1 = colun1.replace("1",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1   
    if resposta == 2:
        os.system('cls')
        if colun1[4] == "2":
            colun1 = colun1.replace("2",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1

    if resposta == 3:
        os.system('cls')
        if colun1[8] == "3":
            colun1 = colun1.replace("3",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1
    if resposta == 4:
        os.system('cls')
        if colun2[0] == "4":
            colun2 = colun2.replace("4",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1
    if resposta == 5:
        os.system('cls')
        if colun2[4] == "5":
            colun2 = colun2.replace("5",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1
    if resposta == 6:
        os.system('cls')
        if colun2[8] == "6":
            colun2 = colun2.replace("6",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1
    if resposta == 7:
        os.system('cls')
        if colun3[0] == "7":
            colun3 = colun3.replace("7",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1
    if resposta == 8:
        os.system('cls')
        if colun3[4] == "8":
            colun3 = colun3.replace("8",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1
    if resposta == 9:
        os.system('cls')
        if colun3[8] == "9":
            colun3 = colun3.replace("9",marcacao)
        else:
            print("Marcação inválida")
            alternancia -= 1
    if resposta == 0:
        break

    alternancia += 1

    printTabela()
    checaVitoria()
