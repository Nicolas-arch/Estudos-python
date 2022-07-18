def usuario():
    DigitouDireito=False
    while not DigitouDireito:
        try:
            idade =int(input('Insira sua idade: '))
            genero=str(input('Qual seu gênero biológico (Masculino ou Feminino): ')).upper()
            peso=int(input('Insira seu peso: '))
            altura=float(input('Insira sua altura em cm: '))
            if idade<0:
                print('Apenas números positivos!')

            elif genero != 'MASCULINO' and genero != 'FEMININO':
                print('Apenas digite Masculino ou Feminino')

            elif peso<0:
                print('Apenas números positivos!')

            elif altura<0:
                print('Apenas números positivos!')

            else:
                DigitouDireito=True


            if genero == 'MASCULINO':
                n1 = 66.5
                p = 13.75 * peso
                at = 5.003 * altura
                e = 6.77 * idade
            elif genero == 'FEMININO':
                n1 = 655.1
                p = 9.56 * peso
                at = 1.85 * altura
                e = 4.68 * idade
        except ValueError:
            print("valores invalidos")

    # Calculo->mulher=665.1+(9.56xp)+(1.85xcm)–(4.7xanos)+atividade
    # Calculo->homem=66.5+(13.75xp)+(5.003xcm)-(6.77xanos)+atividade
            calculo_resultado1=n1+at+p-e
    return (int(calculo_resultado1))


def ingestao_calculo(calculo_resultado):

        alimento=str(input('Que tipo de alimento você ingeriu hoje?: ')).upper()
        quantidade = float(input('Quantos gramas você ingeriu: '))
        if alimento == 'MACARRÃO':
            Diminuição=calculo_resultado-quantidade * 1.57
        elif alimento == 'ARROZ':
            Diminuição=calculo_resultado-quantidade * 1.3
        elif alimento == 'PICANHA':
            Diminuição=calculo_resultado-quantidade * 2.4
        elif alimento == 'BATATA FRITA':
            Diminuição = calculo_resultado - quantidade *  5.2

        return (float(Diminuição))


def calcular_atividade(calculo_resultado):
    alimento=str(input('Que tipo de alimento você ingeriu hoje?: ')).upper()
    quantidade = float(input('Quantos gramas você ingeriu: '))

    if alimento == 'MACARRÃO':
        Diminuição=calculo_resultado-quantidade * 1.57
    elif alimento == 'ARROZ':
        Diminuição=calculo_resultado-quantidade * 1.3
    elif alimento == 'PICANHA':
        Diminuição=calculo_resultado-quantidade * 2.4
    elif alimento == 'BATATA FRITA':
        Diminuição = calculo_resultado - quantidade *  5.2

        return (float(Diminuição))
        


def calcular_atividade(calculo_resultado):

    atividade_nivel = input('Qual o seu nivel de atividade(leve, moderado, elevada, intensa)?:').upper()

    if  atividade_nivel  ==  'LEVE':
        atividade_nivel = (30 * calculo_resultado / 100)+calculo_resultado
    elif atividade_nivel == 'MODERADO':
        atividade_nivel=(50 * calculo_resultado / 100)+calculo_resultado
    elif atividade_nivel == 'ELEVADA':
        atividade_nivel=(75 * calculo_resultado / 100)+calculo_resultado
    elif atividade_nivel == 'INTENSA':
        atividade_nivel=(100 * calculo_resultado / 100)+calculo_resultado

    return (int(atividade_nivel))


def ganhar_o_perder(atividade_nivel):

    meta=input('Quer perder, manter,o ganhar peso?: ')

    if meta == 'perder':
        kcal=atividade_nivel-500
    elif meta == 'manter':
        kcal=atividade_nivel
    elif meta == 'ganhar':
        kcal=atividade_nivel+500







    print('Em ordem de',meta,'peso, seu consumo diário de calorias a mais deveria ser de', int(kcal), '!')


ganhar_o_perder(calcular_atividade(ingestao_calculo(usuario())))