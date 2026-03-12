while True:
    nome = input("Digite seu e-mail: ")
    if nome != "":
        continue
    senha = input("Digite sua senha: ")
    if senha == "":
        break
print("Acesso concedido.")