#Exercício: Calculadora com Tratamento de Exceções
#Crie um programa que funcione como uma calculadora simples. Ele deve solicitar ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão). O programa deve usar try e except para lidar com os seguintes casos:
#Entrada inválida: O usuário digitar algo que não seja um número.
#Divisão por zero: O usuário tentar dividir por zero.
#Operação inválida: O usuário digitar uma operação que não seja válida (+, -, *, /).

print('CALCULADORA')

try:
    primeiroNumero = float(input('Insira o primeiro número: '))
    operador = input('Insira o o operador (+ - * /): ')
    segundoNumero = float(input('Insira o segundo número: '))

    #erro para operadores não válidos
    if operador not in ['+', '-', '*', '/']:
        raise ValueError('Operador inválido! Insira + - * ou /')

    #cálculos
    if operador == '+':
        resultado = primeiroNumero + segundoNumero
    elif operador == '-':
        resultado = primeiroNumero - segundoNumero
    elif operador == '*':
        resultado = primeiroNumero * segundoNumero
    elif operador == '/':
        resultado = primeiroNumero / segundoNumero
    print(f'Resultado: {resultado}')

#erro quando primeiroNumero ou segundoNumero é diferente de um algarismo numérico
except ValueError as erro:
    print(f'Erro: {erro}')
    print('Solução: Insira um número.')

#erro para divisão por zero
except ZeroDivisionError:
    print('Erro: Não é possível dividir por zero.')
