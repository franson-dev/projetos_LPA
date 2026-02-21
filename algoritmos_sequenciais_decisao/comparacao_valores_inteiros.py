"""• Desenvolva um programa que leia dois valores numéricos inteiros 
e compare se o primeiro é maior do que o segundo, 
utilizando uma condicional simples.

• Caso seja (resultado verdadeiro), ele imprime na tela a 
mensagem informando que o primeiro valor digitado é maior do que o segundo."""

# Lê dois valores interiso e compara ambos
print('=' * 30)

x = int(input("Digite um valor inteiro: "))
y = int(input("Digite um segundo valor inteiro: "))

if x > y:
    print(f"O primeiro valor digitado ({x}) é maior do que o segundo valor digitado ({y}).")
    
print('=' * 15)

x = int(input("Digite um valor inteiro: "))
y = int(input("Digite um segundo valor inteiro: "))

if x > y:
    print("O primeiro valor é maior que o segundo valor.")
if x < y:
    print("O segundo valor é maior que o primeiro valor.")
    
print('=' * 15)

# Condicional composta

x = int(input("Digite um valor inteiro: "))
y = int(input("Digite um segundo valor inteiro: "))

if x > y:
    print(f"O {x} é maior que {y}.")
else:
    print(f"O {y} é maior que {x}.")
    
print('=' * 15)

# Desenvolva um programa que leia um valor inteiro e descreva se é par ou ímpar.

x = int(input("Digite um valor inteiro: "))

if x % 2 == 0: 
    print(f"O valor {x} é par.")
else:
    print(f"O valor {x} é impar.")

print("=" * 30)

# Operadores lógicos/booleanos 

    # not
x = True
y = False

print(not x) # False
print(not y) # True

    #and    
x = True
y = False

print(x and y) # False

    # or
x = False
y = False

print(x or y) # False

print("=" * 30)

# Expressões lógicas/booleanas

x = 10
y = 1
res = not x > y

print(res) # False

print("=" * 15)
