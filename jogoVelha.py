import os

colun1 = "1 / 2 / 3"
colun2 = "4 / 5 / 6"
colun3 = "7 / 8 / 9"

marcacao = ""
alternancia = 1

def printTabela():
    print("==================")
    print("Jogo da Velha")
    print(colun1)
    print(colun2)
    print(colun3)
    print("==================")


def mensagemVitoria():
    if (alternancia % 2 == 0):
        print("Vitória do x!")
        os._exit(checaVitoria == True)
    else:
        print("Vitória das bolinhas!") 
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

os.system('cls')
printTabela()

while True:
    resposta = int(input("Aonde você deseja marcar?" ))
    if (alternancia % 2 == 0):
        marcacao = "o"
    else: 
        marcacao = "x"

    if resposta == 1:
        colun1 = colun1.replace("1",marcacao)
    elif resposta == 2:
        colun1 = colun1.replace("2",marcacao)
    elif resposta == 3:
        colun1 = colun1.replace("3",marcacao)
    elif resposta == 4:
        colun2 = colun2.replace("4",marcacao)
    elif resposta == 5:
        colun2 = colun2.replace("5",marcacao)
    elif resposta == 6:
        colun2 = colun2.replace("6",marcacao)
    elif resposta == 7:
        colun3 = colun3.replace("7",marcacao)
    elif resposta == 8:
        colun3 = colun3.replace("8",marcacao)
    elif resposta == 9:
        colun3 = colun3.replace("9",marcacao)
    elif resposta == 0:
        break

    alternancia += 1

    os.system('cls')   
    printTabela()
    checaVitoria()
