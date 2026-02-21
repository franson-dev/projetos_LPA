'''
Exercício:
Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs,
laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções:
1 para maçã, 2 para laranja e 3 para banana.

Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
Considere que uma maçã custa R$ 2,30, uma laranja, R$ 3,60, e uma banana, R$ 1,85.
'''

print("--- MENU DE FRUTAS ---")
print("1 - Maçã (R$ 2,30)")
print("2 - Laranja (R$ 3,60)")
print("3 - Banana (R$ 1,85)")

# Entrada da opção do usuário
opcao = int(input("\nEscolha a opção desejada (1, 2 ou 3): "))

# Verificação da fruta escolhida e definição do preço unitário
if opcao == 1:
    fruta = "Maçã"
    preco_unitario = 2.30
elif opcao == 2:
    fruta = "Laranja"
    preco_unitario = 3.60
elif opcao == 3:
    fruta = "Banana"
    preco_unitario = 1.85
else:
    fruta = None
    print("Opção inválida!")

# Se a opção for válida, prossegue com o cálculo das quantidades
if fruta:
    quantidade = int(input(f"Quantas unidades de {fruta} você deseja comprar? "))
    total = quantidade * preco_unitario
    
    print(f"\nVocê escolheu: {fruta}")
    print(f"Quantidade: {quantidade}")
    print(f"Total a pagar: R$ {total:.2f}")