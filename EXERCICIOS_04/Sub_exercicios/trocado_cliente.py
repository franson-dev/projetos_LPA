valor = int(input("Digite o valor inteiro: "))

# Lista de cédulas disponíveis
cedulas = [100, 50, 20, 10, 5, 1]

print("\nQuantidade de cédulas necessárias:")

for cedula in cedulas:
    qtd = valor // cedula   # divisão inteira
    valor = valor % cedula  # resto da divisão
    if qtd > 0:
        print(f"{qtd} nota(s) de R$ {cedula}")
