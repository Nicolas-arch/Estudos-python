import forca
import jogoAdivinhacao

def tiposJogos():
    print("**********************************")
    print("        Escolha o seu jogo!       ")
    print("**********************************")


    print("(1) Forca \n(2) Adivinhação \n(3) Sair")

    jogo = int(input("\nEscolha seu jogo: \n"))

    if(jogo==1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo==2):
        print("Jogando Adivinhação")
        jogoAdivinhacao.jogar()
    elif jogo==3:
        print("Fim do jogo")
        exit()
    else:
        print("essa opção não existe")
        
if(__name__=="__main__"):
    tiposJogos()