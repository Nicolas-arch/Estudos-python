from errno import EEXIST
import copy
# declaração das variaveis usadas
test = [[0, 3, 2, 28], [4, 0, 2, 24], [2, 3, 0, 16]]
# variavel com o valor do tamanho do array test (nesse caso é 3)
sizeTest = len(test)
# variavel declarada para pegar os pares de linhas
pairs = []

# inicio da geração dos pares
# variavel i que sera usada para controlar o percurso do array
i = 0
# enquanto i for menor que o tamanho do array test (3)
# em suma, o que acontece nesse while é o seguinte: o array test será percorrido por completo, pegando uma linha e criando todos os pares dela, que são basicamente essa linha e a proxima linha, uma a uma, até que acabem as linhas
while(i < sizeTest):
    # a variavel j recebe o valor de i mais 1, isso serve para que possamos pegar o proximo valor do array
    j = i+1
    # enquanto j for menor que o tamanho do array test (3)
    while(j < sizeTest):
        # pega a linha atual
        actual = test[i]
        # pega a proxima linha
        next = test[j]
        # guarda no array pairs os valores da linha, exceto o valor que é o resultado. Por exemplo, a primeira linha é [0, 3, 2, 28], o valor a ser guardado será [0, 3, 2], o 28 não será guardado
        pairs.append([actual[0:len(test[i])-1], next[0:len(test[j])-1]])
        j += 1
    i += 1
i = 0

print(pairs, "Aqui temos todos os pares de linha")

# esse ponto aqui verifica a parte 5 do trabalho (mto grande pra descrever kjfhasjlkfasfa)

# enquanto i for menor que o tamanho do array de pares (quero mapear todos os pares)
while(i < len(pairs)):
    # pega o par atual
    actual = pairs[i]
    # declara j igual a 0, para que a cada loop o j inicie como 0
    j = 0
    # pega os resultados
    result = []
    # enquanto j for menor que o tamanho do primeiro valor inserido no atual
    while(j < len(actual[0])):
        # pega o primeiro valor do atual (que nada mais é o par de linha atual)
        first = actual[0]
        # pega o segundo valor do atual
        second = actual[1]
        # se o valor referente ao valor de j dentro do second, que é o valor de uma linha (por exemplo se o second é [4, 0, 2] e j for 1, o valor de second[j] é 0) for igual a 0
        if(second[j] == 0):
            # insere no result o valor by zero, pq não se pode dividir por zero
            result.append('by zero')
        else:
            # caso a divisão seja possivel, divide o valor referente ao j do first pelo de second  (por exemplo, first = [0,3,2] e second = [4,0,2] e j = 2, a divisão será 2/2) e guarda no result
            result.append(first[j] / second[j])
        j += 1
    # aqui ele verifica se existe valores iguais no result, que guarda os valores dos coeficientes dividos (leia a parte 5 que fica mais claro lá)
    for val in result:
        # se tiver algum valor igual dentro do result
        if(result.count(val) > 1):
            # printa que a expressão é invalida
            print('Expressão invalida')
            break
    i += 1

# nesse ponto aqui iremos fazer a parte 6 e é aqui que o bigode entorta
i = 0
withoutZeroInDiagonal = []
# enquanto i for menor que o sizeTest
while(i < sizeTest):
    # aqui ele vai pegar o array de test e vai fazer um deep copy pq sim
    copyArrayTest = copy.deepcopy(test)

    positionInArray = i
    j = 0
    initialPositionInArray = 0
    while(j < sizeTest):
        k = 0
        l = 0
        # se o positionInArray for do tamanho do sizeTest, ou seja, já chegou no fim do array, ele zera para começar da primeira posição, pq depois da ultima posição n tem nada kkkkkkkkkkkkkk
        if(positionInArray == sizeTest):
            positionInArray = 0
        # pega a linha atual do array de acordo com o positionInArray, que vai ser iterado a cada loop
        actual = copyArrayTest[positionInArray]
        # se o positionInArray mais um for maior ou igual ao size test, ou seja, o proximo valor não existe pq já chegou no limite do array
        if(positionInArray+1 >= sizeTest):
            # o next pega a linha do array test copiado referente ao initialPositionInArray, que inicia com o valor zerado (n ligue mto para os nomes da variavel)
            next = copyArrayTest[initialPositionInArray]
            # insere nessa posição que o valor acabou de ser guardado no next o valor do actual
            copyArrayTest[initialPositionInArray] = actual
            # itera mais um no valor do initialPositionArray
            initialPositionInArray += 1
        else:
            # caso contrario, o next recebe o valor do copy array de acordo com o positivonInArray mais um, pq ainda existe linha a frente do positionInArray
            next = copyArrayTest[positionInArray+1]
            # insere nessa posição que o valor acabou de ser guardado no next o valor do actual
            copyArrayTest[positionInArray+1] = actual

        # insere na posição referente ao positionInArray o proximo valor
        copyArrayTest[positionInArray] = next
        # itera o valor do positionInArray para continuar fazendo o mapeamento da proxima linha
        positionInArray += 1
        j += 1
        # aqui iremos verificar se após fazer a troca das linhas de posição, existe alguma combinação que não tem 0 na diagonal principal
        lastOneCombinationZeroDiagonal = 0

        while(k < sizeTest):
            # pega o item atual de acordo com o valor de k, que é o index no caso
            actualItem = copyArrayTest[k]
            # verifica se o valor referente ao k do actualItem é igual a 0, ou seja, estou pegando o valor da diagonal principal, pq por exemplo, na primeira linha o valor da diagonal principal é o primeiro valor, na segunda o segundo valor, na terceira o terceiro valor e por ai vai
            if(actualItem[k] == 0):
                # se for adiciona 1 ao lastOneCombinationZeroDiagonal
                lastOneCombinationZeroDiagonal += 1
            k += 1
        # se lastOneCombinationZeroDiagonal for igual a 0, significa que nenhum valor entrou no if do while de cima, ou seja, sem zeros na diagonal principal
        if(lastOneCombinationZeroDiagonal == 0):
            # pega esse array e guarda no withoutZeroInDiagonal (pode ser varias combinações)
            withoutZeroInDiagonal.append(copy.deepcopy(copyArrayTest))
    i += 1

# isso aqui quando eu fiz só eu e deus sabiamos o q eu tava fazendo, agora só deus sabe, mas vou tentar explicar o maximo que eu lembro afaslkfjaslkfasfas

i = 0
# para cada array que n tem 0 da diagonal principal ele vai realizar o seguinte:
for arr in withoutZeroInDiagonal:
    # essa é a parte 7
    # pega a primeira linha do array sem zeros na diagonal atual
    controlLine = arr[0]
    # pega o primeiro elemento da primeira linha
    firstLineElement = controlLine[0]
    # enquanto i for menor que o numero de elementos em controlLine
    while(i < len(controlLine)):
        # aqui ele transforma o primeiro elemento da primeira linha em 1, que é o que o enunciado pede
        if(i == 0):
            controlLine[i] = 1
        else:
            # aqui ele verifica se o primeiro elemento da primeira linha é 0, o que nem precisa pq n tem 0 na diagonal principal mas to com preguiça de apagar isso aqui
            if(firstLineElement == 0):
                controlLine[i] = 'by zero'
            else:
                # pega o respectivo elemento da primeira linha, e divide ele mesmo pelo primeiro elemento que tinha antes
                controlLine[i] = controlLine[i] / firstLineElement
        i += 1
    # faz outra copia do array pq sim, n quero ficar sobrescrevendo o mesmo array
    copyArrayArr = copy.deepcopy(arr)

    # esse ponto aqui faz todo o resto de transformar os valores em 0 q n são da diagonal principal e em 1 os valores que são
    n = 0
    while(n < sizeTest):
        # pega a linha referente ao index do valor de n, essa é a linha
        controlLine = copyArrayArr[n]
        # o i, a cada loop, começa com 0
        i = 0

        while(i < len(copyArrayArr)):
            resultLine = []
            # pega a linha referente ao index do valor de i
            actualLine = copyArrayArr[i]
            # pega o elemento da linha atual de acordo com o valor de n (isso aqui é pra pegar sempre o valor da coluna atual, primeira linha primeira coluna, segunda linha primeira coluna e por ai vai para todas linhas e todas colunas)
            element = actualLine[n]
            # se esse elemento for diferente de 0 e i for diferente de n, isso pq se i for igual a n, significa que eu estou pegando o valor da diagonal principal e eu n quero mexer nele
            if(element != 0 and i != n):
                j = 0
                # enquanto j for menor que o valor de elementos de actual line
                # isso aqui vai percorrer toda a linha atual
                while(j < len(actualLine)):
                    # para cada elemento da linha, ele irá multiplicar esse valor pelo primeiro elemento dessa linha negativado
                    resultLine.append(controlLine[j] * (element * -1))
                    j += 1
                k = 0
                while(k < len(actualLine)):
                    # para cada elemento da linha atual, ele irá somar pelo valor da mesma posição que está no result, que são os resultados da multiplicação feita no while de cima, gerando os valores esperados
                    actualLine[k] = actualLine[k] + resultLine[k]
                    k += 1
                # aqui ele vai pegar o valor da diagonal da linha atual
                diagonalValue = actualLine[i]
                # se esse valor for diferente de 1 (n precisa mudar nada) ou 0 (não da pra fazer divisão por 0)
                if(diagonalValue != 1 and diagonalValue != 0):
                    k = 0
                    # enquanto k for menor que o tamanho de actualLine (isso é para mapear toda a linha)
                    while(k < len(actualLine)):
                        # para cada elemento da linha, será feito a divisão do elemento pelo valor da diagonal
                        actualLine[k] = actualLine[k] / diagonalValue
                        k += 1
            i += 1
        n += 1

    # essa parte irá verificar se tem algum 0 na diagonal principalm caso tenha ele tenta calcular outra matriz
    # esse while faz o mesmo que o while lá em cima na linha 106 do algoritmo
    k = 0
    lastOneCombinationZeroDiagonal = 0
    while(k < sizeTest):
        actualItem = copyArrayArr[k]
        if(actualItem[k] == 0):
            lastOneCombinationZeroDiagonal += 1
        k += 1
    # caso n tenha zeros na diagonal principal ele printa os valores
    if(lastOneCombinationZeroDiagonal == 0):
        print('Result:')
        for val in copyArrayArr:
            print(val)
        break
    print("Não tem como calcular essa matriz")
