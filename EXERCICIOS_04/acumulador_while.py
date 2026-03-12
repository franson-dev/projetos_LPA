'''
Escreva um algoritmo que calcule a sua media de notas em determinada disciplina

Vamos assumir que a média final e dada pela media aritmetica de cinco notas digitadas
'''

soma = 0 
cont = 1

while cont <= 5:
    x = float(input(f"Digite a {cont}ª nota: "))
    soma += x
    cont += 1
media = soma / 5
print(f"Media final: {media}")