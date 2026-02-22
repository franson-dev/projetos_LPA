# Escreva as seguintes expressões booleanas em linguagem Python:

'''
- Expressões booleanas
a) O somatório de 2 com 2 é menor que 4
b) O valor 7 // 3 é igual a 1 + 1
c) A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
d) A soma de 2, 4 e 6 é maior que 12
e) 1387 é divisível por 19
f) 31 é par
g) O menor valor entre 34, 29 e 31 é menor que 30
'''

# a)

if (2 + 2) < 4:
    print("O somatório de 2 com 2 é menor que 4.")

print("=" * 30)

# b)

if (7 // 3) == (1 + 1):
    print("O valor 7 // 3 é igual a 1 + 1.")

print("=" * 30)

# c)

if (3**2 + 4**2) == 25:
    print("A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25.")

print("=" * 30)

# d)

if (2 + 4 + 6) > 12:
    print("A soma de 2, 4 e 6 é maior que 12.")

print("=" * 30)

# e)

if (1387 % 19) == 0:
    print("1387 é divisível por 19.")

print("=" * 30)

# f)

if (31 % 2) == 0:
    print("31 é par.")
else:
    print("31 é impar.")

print("=" * 30)

# g)

if min(34, 29, 31) < 30:
    print("O menor valor entre 34, 29 e 31 é menor que 30.")

print("=" * 30)

'''- Condicional Simples
h) Se idade é maior que 60, escreva: "Você tem direitos aos benefícios"
i) Se dano é maior que 10 e escudo é igual a 0, escreva: "Você morreu"
j) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em Tru, escreva: "Você escapou"
'''

# h)

idade = int(input("Digite sua idade: "))


if idade > 60:
    print("Você tem direitos aos benefícios.")

print("=" * 30)

# i)

dano = int(input("Digite o valor do dano: "))
escudo = int(input("Digite o valor do escudo: "))

if (dano > 10) and (escudo == 0):
    print("Você morreu.")

print("=" * 30)

# j)

norte = True
sul = False
leste = False
oeste = False

if norte or sul or leste or oeste:
    print("Você escapou.")

print("=" * 30)

'''
- Condicional Composta
k) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto", caso contrário, escreva: "Não é um ano bissexto"
l) Se ambas as variáveis booleanas cima e baixo forem True, escreva: "Você escolheu um caminho!"

'''

# k)

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Pode ser um ano bissexto.")
else:
    print("Não é um ano bissexto.")

print("=" * 30)

# l)

cima = True
baixo = True

if cima and baixo:
    print("Você escolheu um caminho!")

print("=" * 30)

'''
- Exercício 1:
Faça um algoritmo que receba três valores, representando os lados de um triângulo
fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
1) Equilátero (três lados iguais)
2) Isósceles (dois lados iguais)
3) Escaleno (três lados diferentes)
'''

# Entrada dos lados
A = float(input("Digite o primeiro lado (A): "))
B = float(input("Digite o segundo lado (B): "))
C = float(input("Digite o terceiro lado (C): "))

# Para ser um triângulo, a soma de dois lados deve ser sempre maior que o terceiro
if (A > 0 and B > 0 and C > 0) and (A + B > C) and (A + C > B) and (B + C > A):
    print("Os valores formam um triângulo!")

    # Classificação
    if A == B == C:
        print("Tipo: Equilátero")
    elif A == B or A == C or B == C:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")
else:
    print(
        "Ao menos um dos valores não é maior que zero ou os valores não podem formar um triângulo."
    )

print("=" * 30)

'''
Exercício 2:
Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário
qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*)
ou divisão (/). Exiba na tela o resultado da operação desejada.
''' 

# Entrada dos valores numéricos
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

# Menu de operações
print("\nOperações disponíveis:")
print("+ : Adição")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")

operacao = input("\nQual operação deseja realizar? ")

# Lógica de seleção da operação usando elif
if operacao == '+':
    resultado = v1 + v2
    print(f"Resultado: {v1} + {v2} = {resultado}")
elif operacao == '-':
    resultado = v1 - v2
    print(f"Resultado: {v1} - {v2} = {resultado}")
elif operacao == '*':
    resultado = v1 * v2
    print(f"Resultado: {v1} * {v2} = {resultado}")
elif operacao == '/':
    # Verificação para evitar divisão por zero
    if v2 != 0:
        resultado = v1 / v2
        print(f"Resultado: {v1} / {v2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")
else:
    print("Operação inválida!")
    
print("=" * 30)

'''
Exercício 3:
Calcule o preço da energia elétrica de acordo com a tabela:
- Residencial: Até 500 kWh (R$ 0,40) | Acima de 500 kWh (R$ 0,65)
- Comercial: Até 1000 kWh (R$ 0,55) | Acima de 1000 kWh (R$ 0,60)
- Industrial: Até 5000 kWh (R$ 0,55) | Acima de 5000 kWh (R$ 0,60)
'''

print("--- CÁLCULO DE CONTA DE ENERGIA ---")
consumo = float(input("Quantidade de kWh consumida: "))
print("Tipos: R (Residencial), C (Comercial), I (Industrial)")
tipo = input("Tipo de instalação: ").upper()

# Lógica de decisão baseada na tabela da aula
if tipo == 'R':
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'C':
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'I':
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Erro: Tipo de instalação inválido!")

if preco > 0:
    total = consumo * preco
    print(f"Preço por kWh: R$ {preco:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
