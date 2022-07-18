
# forca.py
from operator import truediv
import forca
import jogos

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


    palavraSecreta="banana";
    enforcou=False
    acertou=False
    #enquanto nao enforcou(true) e nao acerotu(true)
    while(not enforcou and not acertou):
        chute=input("Qual a letra:")
        for letra in palavraSecreta:
            if(chute==letra):
                print(chute)


'''
    print("o que deseja fazer?")
    print(" (1) jogar novamente \n (2) escolher outro jogo \n (3) sair")

    opcao= int(input("escolha: "))

    if (opcao == 1):
        forca.jogar()
    elif(opcao==2):
        jogos.tiposJogos()
    elif(opcao==3):
        print("Fim do jogo")
        exit()
        
    elif (opcao<1 or opcao>3):
        print("essa opção não existe")
        print("Fim do jogo")
'''
if(__name__=="__main__"):
    jogar()