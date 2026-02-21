""" Desenvolva um algoritmo que solicite ao usuário 
o preço de um produto e um percentual de desconto a ser
aplicado a ele. Calcule e exiba o valor do desconto e o 
preço final do produto. """

preco = float(input("Digite o preço do produto: "))
desconto_percentual = float(input("Digite o percentual de desconto: "))

desconto_valor = preco * (desconto_percentual / 100)
preco_final = preco - desconto_valor

print(f"Valor do desconto: R$ {desconto_valor:.2f}")
print(f"Preço final do produto: R$ {preco_final:.2f}, com desconto de {desconto_percentual:.0f}%")