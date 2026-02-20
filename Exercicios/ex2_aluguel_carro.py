"""Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias
pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado."""

km = int(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

preco_km = 60 * dias + 0.15 * km

print(f"Km = {km} km")
print(f"Dias = {dias} dias")
print(f"Preço a pagar: R$ {preco_km:.2f}")
