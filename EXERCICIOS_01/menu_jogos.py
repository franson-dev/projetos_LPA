import random
import time

def mostrar_menu():
    """Mostra o menu principal de jogos"""
    print("\n" + "=" * 50)
    print("🎮 BEM-VINDO AO MENU DE JOGOS! 🎮")
    print("=" * 50)
    print("1. Jogo da Forca")
    print("2. Meu Nome em uma Frase")
    print("3. Calculadora")
    print("4. Jogo do Diamante")
    print("5. Produtos de Loja com Desconto")
    print("6. Empréstimo com Juros")
    print("7. Calculadora de Gasolina")
    print("0. Sair")
    print("=" * 50)

def jogo_da_forca():
    """Jogo da Forca - Adivinhe a palavra"""
    print("\n🎯 JOGO DA FORCA 🎯")
    
    palavras = [
        "PYTHON", "PROGRAMACAO", "COMPUTADOR", "TECNOLOGIA", 
        "DESENVOLVIMENTO", "ALGORITMO", "SOFTWARE", "ALGORITMO",
        "JOGO", "DESAFIO", "FUNCAO", "VARIAVEL", "BIBLIOTECA"
    ]
    
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_"] * len(palavra_secreta)
    tentativas = 6
    letras_usadas = []
    
    print(f"A palavra tem {len(palavra_secreta)} letras")
    print(" ".join(letras_descobertas))
    
    while tentativas > 0:
        letra = input("\nDigite uma letra: ").upper()
        
        if letra in letras_usadas:
            print("Você já usou essa letra!")
            continue
        
        letras_usadas.append(letra)
        
        if letra in palavra_secreta:
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_descobertas[i] = letra
            print("✅ Letra correta!")
        else:
            tentativas -= 1
            print(f"❌ Letra incorreta! Tentativas restantes: {tentativas}")
        
        print(" ".join(letras_descobertas))
        
        if "_" not in letras_descobertas:
            print(f"\n🎉 PARABÉNS! Você acertou a palavra: {palavra_secreta}!")
            break
    
    if tentativas == 0:
        print(f"\n💀 Você perdeu! A palavra era: {palavra_secreta}")

def meu_nome_frase():
    """Exibe o nome do usuário em uma frase criativa"""
    print("\n📝 MEU NOME EM UMA FRASE 📝")
    nome = input("Digite seu nome: ")
    
    frases = [
        f"{nome} é uma pessoa incrível que está aprendendo programação!",
        f"Olá, {nome}! Você está no caminho certo para se tornar um desenvolvedor!",
        f"{nome} - um nome que significa sucesso e determinação!",
        f"Bem-vindo, {nome}! Cada dia é uma nova oportunidade de aprender!",
        f"{nome} está criando um futuro brilhante com a tecnologia!"
    ]
    
    print("\n✨ SUA FRASE ESPECIAL ✨")
    print("-" * 40)
    print(random.choice(frases))
    print("-" * 40)

def calculadora():
    """Calculadora simples com as 4 operações básicas"""
    print("\n🔢 CALCULADORA 🔢")
    
    print("Escolha a operação:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    opcao = input("Digite a opção (1-4): ")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == "1":
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"\nResultado: {num1} * {num2} = {resultado}")
        elif opcao == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado: {num1} / {num2} = {resultado}")
            else:
                print("\n❌ Erro: Divisão por zero!")
        else:
            print("\n❌ Opção inválida!")
    except ValueError:
        print("\n❌ Erro: Digite números válidos!")

def jogo_diamante():
    """Jogo do Diamante - Escolha a porta certa para ganhar o diamante"""
    print("\n💎 JOGO DO DIAMANTE 💎")
    print("=" * 40)
    print("Você está em uma sala com 3 portas.")
    print(" atrás de uma porta há um diamante valioso!")
    print(" atrás das outras duas portas há... nada!")
    print("=" * 40)
    
    porta_correta = random.randint(1, 3)
    
    print("\nPorta 1 🚪  |  Porta 2 🚪  |  Porta 3 🚪")
    print("Escolha uma porta (1, 2 ou 3)")
    
    escolha = input("Sua escolha: ")
    
    try:
        escolha = int(escolha)
        if escolha < 1 or escolha > 3:
            print("\n❌ Escolha inválida! Debe ser 1, 2 ou 3.")
            return
        
        print("\nAbrindo a porta...")
        time.sleep(1)
        print("🎲 suspense...")
        time.sleep(1)
        
        if escolha == porta_correta:
            print("\n🎉 PARABÉNS! Você encontrou o diamante! 💎")
            print("Você ganhou o prêmio de 1 milhão de dólares!")
        else:
            print("\n😞 Que pena! A porta correta era a", porta_correta)
            print("O diamante estava lá! Mas não desanime, tente novamente!")
    except ValueError:
        print("\n❌ Erro: Digite um número válido!")

def produtos_loja():
    """Calcula desconto em produtos de uma loja"""
    print("\n🛒 PRODUTOS DE LOJA COM DESCONTO 🛒")
    print("=" * 40)
    
    produtos = {
        "1": {"nome": "Notebook", "preco": 3500.00},
        "2": {"nome": "Smartphone", "preco": 2500.00},
        "3": {"nome": "Fone de Ouvido", "preco": 299.00},
        "4": {"nome": "Smartwatch", "preco": 899.00},
        "5": {"nome": "Tablet", "preco": 1800.00},
        "6": {"nome": "Televisor 50\"", "preco": 3200.00}
    }
    
    print("Lista de Produtos:")
    for key, value in produtos.items():
        print(f"{key}. {value['nome']}: R$ {value['preco']:.2f}")
    
    print("\n7. Digitar outro produto")
    
    opcao = input("\nEscolha o produto (1-7): ")
    
    if opcao in produtos:
        produto = produtos[opcao]
        nome = produto["nome"]
        preco = produto["preco"]
    elif opcao == "7":
        nome = input("Digite o nome do produto: ")
        try:
            preco = float(input("Digite o preço do produto: R$ "))
        except ValueError:
            print("❌ Erro: Preço inválido!")
            return
    else:
        print("❌ Opção inválida!")
        return
    
    print(f"\nProduto: {nome}")
    print(f"Preço original: R$ {preco:.2f}")
    
    print("\nEscolha o desconto:")
    print("1. 5% (5 reais a cada 100)")
    print("2. 10%")
    print("3. 15%")
    print("4. 20%")
    print("5. 25%")
    print("6. 50%")
    
    desc_opcao = input("Escolha o desconto (1-6): ")
    
    descontos = {"1": 5, "2": 10, "3": 15, "4": 20, "5": 25, "6": 50}
    
    if desc_opcao in descontos:
        percentual = descontos[desc_opcao]
        valor_desconto = preco * (percentual / 100)
        preco_final = preco - valor_desconto
        
        print("\n" + "=" * 40)
        print(f"Produto: {nome}")
        print(f"Preço original: R$ {preco:.2f}")
        print(f"Desconto: {percentual}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"✅ PREÇO COM DESCONTO: R$ {preco_final:.2f}")
        print("=" * 40)
    else:
        print("❌ Opção de desconto inválida!")

def emprestimo_juros():
    """Calcula empréstimo com juros"""
    print("\n💰 EMPRÉSTIMO COM JUROS 💰")
    print("=" * 40)
    
    try:
        valor = float(input("Digite o valor do empréstimo: R$ "))
        print("\nEscolha o período:")
        print("1. 3 meses (5% ao mês)")
        print("2. 6 meses (4.5% ao mês)")
        print("3. 12 meses (4% ao mês)")
        print("4. 24 meses (3.5% ao mês)")
        
        periodo_opcao = input("Escolha o período (1-4): ")
        
        periodos = {
            "1": {"meses": 3, "juros": 5.0},
            "2": {"meses": 6, "juros": 4.5},
            "3": {"meses": 12, "juros": 4.0},
            "4": {"meses": 24, "juros": 3.5}
        }
        
        if periodo_opcao in periodos:
            meses = periodos[periodo_opcao]["meses"]
            taxa_juros = periodos[periodo_opcao]["juros"]
            
            # Cálculo de juros compostos
            valor_final = valor * ((1 + taxa_juros/100) ** meses)
            total_juros = valor_final - valor
            valor_mensal = valor_final / meses
            
            print("\n" + "=" * 40)
            print("📊 RESUMO DO EMPRÉSTIMO")
            print("=" * 40)
            print(f"Valor solicitado: R$ {valor:.2f}")
            print(f"Período: {meses} meses")
            print(f"Taxa de juros: {taxa_juros}% ao mês")
            print(f"Valor total a pagar: R$ {valor_final:.2f}")
            print(f"Total de juros: R$ {total_juros:.2f}")
            print(f"Valor mensal: R$ {valor_mensal:.2f}")
            print("=" * 40)
        else:
            print("❌ Opção de período inválida!")
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def calculadora_gasolina():
    """Calcula o custo de combustível"""
    print("\n⛽ CALCULADORA DE GASOLINA ⛽")
    print("=" * 40)
    
    try:
        preco_gasolina = float(input("Digite o preço da gasolina (por litro): R$ "))
        preco_alcool = float(input("Digite o preço do álcool (por litro): R$ "))
        
        print("\nQual combustível você deseja usar?")
        print("1. Gasolina")
        print("2. Álcool")
        
        combustivel = input("Escolha (1-2): ")
        
        if combustivel == "1":
            tipo = "Gasolina"
            preco = preco_gasolina
        elif combustivel == "2":
            tipo = "Álcool"
            preco = preco_alcool
        else:
            print("❌ Opção inválida!")
            return
        
        distancia = float(input("\nDigite a distância a percorrer (km): "))
        consumo = float(input("Digite o consumo do carro (km por litro): "))
        
        litros_necessarios = distancia / consumo
        custo_total = litros_necessarios * preco
        
        print("\n" + "=" * 40)
        print("⛽ RESUMO DA VIAGEM")
        print("=" * 40)
        print(f"Combustível: {tipo}")
        print(f"Preço por litro: R$ {preco:.2f}")
        print(f"Distância: {distancia} km")
        print(f"Consumo do carro: {consumo} km/L")
        print(f"Litros necessários: {litros_necessarios:.2f} L")
        print(f"✅ CUSTO TOTAL: R$ {custo_total:.2f}")
        print("=" * 40)
        
        # Comparação entre gasolina e álcool
        if preco_alcool > 0 and preco_gasolina > 0:
            razao = preco_alcool / preco_gasolina
            print(f"\n💡 Análise: O álcool está a {razao*100:.1f}% do preço da gasolina")
            if razao <= 0.7:
                print("→ Álcool compensa mais!")
            else:
                print("→ Gasolina compensa mais!")
                
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos!")

def main():
    """Função principal do programa"""
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            jogo_da_forca()
        elif opcao == "2":
            meu_nome_frase()
        elif opcao == "3":
            calculadora()
        elif opcao == "4":
            jogo_diamante()
        elif opcao == "5":
            produtos_loja()
        elif opcao == "6":
            emprestimo_juros()
        elif opcao == "7":
            calculadora_gasolina()
        elif opcao == "0":
            print("\n👋 Obrigado por usar o Menu de Jogos! Até mais!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
