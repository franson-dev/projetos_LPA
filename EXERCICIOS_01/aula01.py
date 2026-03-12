print("-" * 30)
print("O começo de tudo:")
print("Hello, World!")
print("-" * 30)
print("Opções Aritméticas:")
print("o resultado de 2 + 3 é:", 2 + 3)
print("o resultado de 10 - 4 é:", 10 - 4)
print("-" * 30)
print("Ordem de Precedência:")
print(10 * (5 + 7 / 4))
print("-" * 30)
print("Variáveis:")
nota = 8.5
disciplina = "Lógica de Programação e Algoritmos"

print(nota)
print(disciplina)
print("Disciplina:", disciplina, ". Nota:", nota)
print("-" * 30)
print("Tipos de Dados:")
a = 1
b = 5
resposta = a == b
print(resposta)
resposta = a != b
print(resposta)
print("-" * 30)
print("Strings:")
frase = "Olá, mundo!"
print(frase)
print("-" * 30)
print("Concatenando Strings:")
s1 = "Logica de Programação"
s1 = s1 + " e Algoritmos"
print(s1)
print("-" * 10)
s1 = "A" + "-" * 10 + "B"
print(s1)
print("-" * 10)
s1 = "A" + " " * 10 + "B"
print(s1)
print("-" * 30)
print("Formatando Strings:")
nota = 8.5
s1 = "Você tirou %f na disciplina de algoritmos." % nota
""" 
- %f é um marcador de posição para um número de ponto flutuante. 
- %d ou %i são marcadores de posição para números inteiros.
- %s é um marcador de posição para strings.
- %r é um marcador de posição para a representação de string de um objeto. 
"""
print(s1)
print("-" * 10)
nota = 8.5
s1 = "Você tirou %.2f na disciplina de algoritmos." % nota
print(s1)
print("-" * 10)
nota = 8.5
disciplina = "Algoritmos"
s1 = "Você tirou %.2f na discplina de %s" % (nota, disciplina)
print(s1)
print("-" * 30)
print("Formatando Strings com .format(Composição moderna):")
nota = 8.5
disciplina = "Algoritmos"
s1 = "Você tirou {} na disciplina de {}".format(nota, disciplina)
print(s1)
print("-" * 30)
print("Formatando Strings com f-strings (Composição moderna):")
nota = 8.5
disciplina = "Algoritmos"
s1 = f"Você tirou {nota} na disciplina de {disciplina}"
print(s1)
print("-" * 30)
print("Fatiamento de Strings:")
s1 = "Lógica de Programação e Algoritmos"
print(s1[0:6])
print(s1[24:34])
print(s1[:6])
print("-" * 30)
print("Tamanho (length):")
s1 = "Lógica de Programação e Algoritmos"
tamanho = len(s1)
print(tamanho)
print("-" * 30)
print("Entrada de Dados:")
idade = input("Digite sua idade: ")
print(f"Sua idade é: {idade}")
print("-" * 10)
nome = input("Digite seu nome: ")
print(f"Olá, {nome}")
print("-" * 10)
nota = float(input("Digite sua nota: "))
print(f"Sua nota é: {nota}")
print("-" * 30)
print("Convertendo dados de entrada(casting):")
nota = float(input("Digite sua nota: "))
print(f"Sua nota é: {nota}")
print("-" * 30)