from select import select


def soma(primeiro_parametro, segundo_parametro):
    return primeiro_parametro + segundo_parametro


def multiplica(primeiro_parametro, segundo_parametro):
    return primeiro_parametro * segundo_parametro


def divide(primeiro_parametro, segundo_parametro):
       try:
           if segundo_parametro == 0.0:
               segundo_parametro = repeticao_de_zero()
           return primeiro_parametro / segundo_parametro
       except ZeroDivisionError:
           'Não é possivel dividir por 0'


def repeticao_de_zero():
    valor_de_zero = input('Não é possivel dividir por 0.\nDeseja informar outro valor? sim(s)/não(n): ')
    if valor_de_zero == 's':
        novo_valor_do_segundo_parametro = segundo_valor_do_parametro()
        if novo_valor_do_segundo_parametro == 0.0:
             return repeticao_de_zero()
        return novo_valor_do_segundo_parametro
    elif valor_de_zero == 'n':
        centro()


def subtrai(parametro1, parametro2):
    return parametro1 - parametro2


def chama_operacao(select):
    return int(input('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair\nInforme a operação? '))


SELECAO = {1: soma, 2: multiplica, 3: divide, 4: subtrai}


def primeiro_valor_do_parametro():
    return float(input(f'Informe o primeiro valor que você deseja calcular: '))


def segundo_valor_do_parametro():
    return float(input(f'Informe o segundo valor que você deseja calcular: '))


def devolve_resultado(operador, primeiro_parametro, segundo_parametro):
    result = SELECAO[operador](primeiro_parametro, segundo_parametro)
    return result


def continua_conta(terceiro_parametro):
    operador = chama_operacao(select)
    primeiro_parametro = terceiro_parametro
    segundo_parametro = segundo_valor_do_parametro()
    terceiro_parametro = devolve_resultado(operador, primeiro_parametro, segundo_parametro)
    print(terceiro_parametro)

    seg = input('Deseja continuar? s/n ')
    if seg == 's':
        continua_conta(terceiro_parametro)
    elif seg == 'n':
        centro()


def centro():
    while 'sim'.title():

        print('Calculadora 1.0\n')

        operador = chama_operacao(select)
        primeiro_parametro = primeiro_valor_do_parametro()
        segundo_parametro = segundo_valor_do_parametro()
        terceiro_parametro = devolve_resultado(operador, primeiro_parametro, segundo_parametro)
        print(terceiro_parametro)

        seg = input('Deseja continuar, fazer nova conta ou finalizar? continuar(c)/nova conta(n)/ finalizar(f):  ')
        if seg == 'c':
            continua_conta(terceiro_parametro)
        elif seg == 'n':
            centro()
        elif seg == 'f':
            break


centro()