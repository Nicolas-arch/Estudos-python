# 2x+3y=28
# 4x+2z=24
# 3y+2x=16

from calendar import c
from re import A, T
from tkinter import E


# equacoes = ['2x+3y=28', '4x+2z=24', '3y+2x=16']
# equacoes = ['2x+3y=28']
equacoes = ['4x+2z=24']
# equacoes = ['3y+2x=16']

def verificar(array):
    for e in array:
        # print(e)
        
        x=False
        y=False
        z=False

        a = e.split('=')[0].split("+")
        for i in a:
            if "x" in i:
                x=True
            if "y" in i:
                y=True
            if "z" in i:
                z=True
        completar(x,y,z,a)
        
def completar(x,y,z,equacao):
    if x == False:
        equacao.append("0x")
    if y == False:
        equacao.append("0y")
    if z == False:
        equacao.append("0z")
    ordenar(equacao)

def ordenar(equacao):
    print(equacao)
    # 0=x
    # 1=y
    # 2=z
    times = 0
    for i in equacao:
        if "x" in i:
            equacao[0] = i
            times += 1
        if "y" in i:
            equacao[1] = i
            times += 1 
        if "z" in i:
            equacao[2] = i
            times += 1

    print(equacao)


    
verificar(array=equacoes)

def carregaMatriz (nomeArq):
    arq     = open(nomeArq,"r")
    qtdLins = int (arq.readline())
    
    ret = []
    for lin in range(qtdLins):
        texto = arq.readline().split()
        
        linha = []
        for col in range(qtdLins+1): linha.append(float(texto[col])) 
            
        ret.append(linha)
        
    arq.close()
    return ret
    
# função auxiliar  recursiva que, de fato, gera as permutacoes
# NÃO USE DIRETAMENTE ESTA FUNÇÃO; USE A FUNÇÃO permutacoes
# recebe uma lista com os valores a serem permutados (linha),
# uma lista com os itens na permutação sendo gerada (perm) e
# uma lista com as permutações geradas (perms) 
def permuta (linha, perm, perms):
    if linha==[]:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin]+linha[lin+1:len(linha)],perm+[linha[lin]],perms)

# função principal para gerar permutações;
# USA A FUNÇÃO permuta, QUE NÃO DEVE SER USADA DIRETAMENTE;
# recebe uma lista com os valores a serem permutados (linha)
# retorna as permutações geradas
def permutacoes (linha):
    perms=[]
    permuta(linha,[],perms)
    return perms
    
def combinacoesDeLinhas2a2 (m):
    ret = []
    for lin in range(len(m)):
        for col in range(lin+1,len(m)):
            ret.append([lin,col])
    return ret
    
def haZeroNaDiagonal (m,ordL,ordC):
    qtdDeZeros=0
    posicao=0
    while posicao<len(m):
        if m[ordL[posicao]][ordC[posicao]]==0: qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
   
def comoSeLivrarDeZerosNaDiagonal (m):
    perms = permutacoes(list(range(len(m))))

    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(m,perms[i],perms[j]):
                return [perms[i],perms[j]];

    return None
'''
matriz = carregaMatriz("sis01.txt")
print (matriz)
print (permutacoes(list(range(len(matriz)))))
print (combinacoesDeLinhas2a2(matriz))
'''

matriz = [[0,0,5,1],\
          [9,0,0,7],\
          [0,6,0,9]]
          
print(comoSeLivrarDeZerosNaDiagonal(matriz))