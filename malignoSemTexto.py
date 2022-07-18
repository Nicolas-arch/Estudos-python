from cgi import test
from errno import EEXIST
import copy


#declarando as variaveis
test = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for l in range(0,3):
    for c in range (0,4):
        test[l][c]= int(input(f' Digite um valor para [{l},{c}]: '))

print(test)

sizeTest = len(test)
pairs = []
i = 0
while(i < sizeTest):
    j = i+1
    while(j < sizeTest):
        actual = test[i]
        next = test[j]
        pairs.append([actual[0:len(test[i])-1], next[0:len(test[j])-1]])
        j += 1
    i += 1
i = 0

print(pairs, "Aqui temos todos os pares de linha")
while(i < len(pairs)):
    actual = pairs[i]
    j = 0
    result = []
    while(j < len(actual[0])):
        first = actual[0]
        second = actual[1]
        if(second[j] == 0):
            result.append('by zero')
        else:
            result.append(first[j] / second[j])
        j += 1
    for val in result:
        if(result.count(val) > 1):
            print('Expressão invalida')
            break
    i += 1

i = 0

withoutZeroInDiagonal = []

while(i < sizeTest):
    copyArrayTest = copy.deepcopy(test)

    positionInArray = i
    j = 0
    initialPositionInArray = 0
    while(j < sizeTest):
        k = 0
        l = 0
        if(positionInArray == sizeTest):
            positionInArray = 0
        actual = copyArrayTest[positionInArray]
        if(positionInArray+1 >= sizeTest):
            next = copyArrayTest[initialPositionInArray]
            copyArrayTest[initialPositionInArray] = actual
            initialPositionInArray += 1
        else:
            next = copyArrayTest[positionInArray+1]
            copyArrayTest[positionInArray+1] = actual

        copyArrayTest[positionInArray] = next
        positionInArray += 1
        j += 1
        lastOneCombinationZeroDiagonal = 0

        while(k < sizeTest):
            actualItem = copyArrayTest[k]
            if(actualItem[k] == 0):
                lastOneCombinationZeroDiagonal += 1
            k += 1
        if(lastOneCombinationZeroDiagonal == 0):
            withoutZeroInDiagonal.append(copy.deepcopy(copyArrayTest))
    i += 1


i = 0
for arr in withoutZeroInDiagonal:
    controlLine = arr[0]
    firstLineElement = controlLine[0]
    while(i < len(controlLine)):
        if(i == 0):
            controlLine[i] = 1
        else:
            if(firstLineElement == 0):
                controlLine[i] = 'by zero'
            else:
                controlLine[i] = controlLine[i] / firstLineElement
        i += 1
    copyArrayArr = copy.deepcopy(arr)

    n = 0
    while(n < sizeTest):
        controlLine = copyArrayArr[n]
        i = 0

        while(i < len(copyArrayArr)):
            resultLine = []
            actualLine = copyArrayArr[i]
            element = actualLine[n]
            if(element != 0 and i != n):
                j = 0
                while(j < len(actualLine)):
                    resultLine.append(controlLine[j] * (element * -1))
                    j += 1
                k = 0
                while(k < len(actualLine)):
                    actualLine[k] = actualLine[k] + resultLine[k]
                    k += 1
                diagonalValue = actualLine[i]
                if(diagonalValue != 1 and diagonalValue != 0):
                    k = 0
                    while(k < len(actualLine)):
                        actualLine[k] = actualLine[k] / diagonalValue
                        k += 1
            i += 1
        n += 1
    k = 0
    lastOneCombinationZeroDiagonal = 0
    while(k < sizeTest):
        actualItem = copyArrayArr[k]
        if(actualItem[k] == 0):
            lastOneCombinationZeroDiagonal += 1
        k += 1
    if(lastOneCombinationZeroDiagonal == 0):
        print('Result:')
        for val in copyArrayArr:
            print(val)
        break
    print("Não tem como calcular essa matriz")