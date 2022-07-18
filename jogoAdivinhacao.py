
from cgitb import reset
import random
import forca
import jogoAdivinhacao
import jogos


def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("**********************************")



    numero_secreto = 42   #0.0 e 1.0
    totalTentativas=3
    rodada=1


    print("Qual nivel de dificuldade?")
    print(" (1) Facil \n (2) Medio \n (3) Dificil")

    nivel= int(input("Defina o nivel: "))

    if(nivel==1):
        totalTentativas=3;
        numero_secreto =  int(round(random.randrange(11)));
        pontos= 10

        for rodada in range(1,totalTentativas+1):
            print("Tentativa {} de {}\n".format(rodada,totalTentativas));
            chute = int(input("Digite um numero de 1 a 10: "));
            print("Voce digitou: {}\n ".format(chute));

            if(chute<1 or chute>10):
                print("voce deve digitar um numero entre 1 e 10");
                continue
            acertou   =numero_secreto==chute;
            chuteMaior=chute>numero_secreto;
            chuteMenor=chute<numero_secreto;

            if acertou:
                print("voce acertou e fez {} pontos!!\n".format(pontos));
                break
            elif(chuteMaior):
                print("voce errou! seu chute foi maior que o numero secreto\n");
            elif(chuteMenor):
                print("voce errou! seu chute foi menor que o numero secreto\n");
            pontosPerdidos = abs(numero_secreto - chute)
            pontos = pontos-pontosPerdidos
        
            
            rodada=rodada+1

        print("o numero secreto era {}".format(numero_secreto))
        print("!!!!!!!!!!!fim do programa!!!!!!")

    elif(nivel==2):
        totalTentativas=5
        numero_secreto =  int(round(random.randrange(51)));
        pontos=50
        for rodada in range(1,totalTentativas+1):
            print("Tentativa {} de {}\n".format(rodada,totalTentativas));
            chute = int(input("Digite um numero de 1 a 50: "));
            print("Voce digitou: {}\n ".format(chute));

            if(chute<1 or chute>100):
                print("voce deve digitar um numero entre 1 e 50");
                continue
            acertou   =numero_secreto==chute;
            chuteMaior=chute>numero_secreto;
            chuteMenor=chute<numero_secreto;

            if acertou:
                print("voce acertou e fez {} pontos!!\n".format(pontos));
                break
            elif(chuteMaior):
                print("voce errou! seu chute foi maior que o numero secreto\n");
            elif(chuteMenor):
                print("voce errou! seu chute foi menor que o numero secreto\n");
            pontosPerdidos = abs(numero_secreto - chute)
            pontos = pontos-pontosPerdidos
            
            rodada=rodada+1

        print("o numero secreto era {}".format(numero_secreto))
        print("!!!!!!!!!!!fim do programa!!!!!!")

    elif nivel==3:
        totalTentativas=10
        pontos=100
        numero_secreto =  int(round(random.randrange(101)));
        for rodada in range(1,totalTentativas+1):
            print("Tentativa {} de {}\n".format(rodada,totalTentativas));
            chute = int(input("Digite um numero de 1 a 100: "));
            print("Voce digitou: {}\n ".format(chute));

            if(chute<1 or chute>100):
                print("voce deve digitar um numero entre 1 e 100");
                continue
            acertou   =numero_secreto==chute;
            chuteMaior=chute>numero_secreto;
            chuteMenor=chute<numero_secreto;

            if acertou:
                print("voce acertou e fez {} pontos!!\n".format(pontos));
                break
            elif(chuteMaior):
                print("voce errou! seu chute foi maior que o numero secreto\n");
            elif(chuteMenor):
                print("voce errou! seu chute foi menor que o numero secreto\n");
            pontosPerdidos = abs(numero_secreto - chute)
            pontos = pontos-pontosPerdidos
            
            rodada=rodada+1

        print("o numero secreto era {}".format(numero_secreto))
        print("!!!!!!!!!!!fim do programa!!!!!!")
    elif (nivel<1 or nivel>3):
        print("voce deve digitar um numero entre 1 e 3");
    
    print("o que deseja fazer?")
    print(" (1) jogar novamente \n (2) escolher outro jogo \n (3) sair")

    opcao= int(input("escolha: "))

    if (opcao == 1):
        jogoAdivinhacao.jogar()
    elif(opcao==2):
        jogos.tiposJogos()
    elif(opcao==3):
        print("Fim do jogo")
        exit()
    elif (opcao<1 or opcao>3):
        print("essa opção não existe")
        


    

if(__name__=="__main__"):
    jogar()



