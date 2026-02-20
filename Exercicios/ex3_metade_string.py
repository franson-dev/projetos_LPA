"""Crie uma variável de string que receba uma frase qualquer. 
Crie uma segunda variável,agora contendo a metade da string digitada. 
Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string."""

frase = input("Digite uma frase qualquer: ")
metade_frase = frase[:len(frase) // 2]
ultimos_dois_caracteres = metade_frase[-2:]

print(f"Frase digitada: {frase}")
print(f"Metade da frase: {metade_frase}")
print(f"Últimos dois caracteres da metade da frase: {ultimos_dois_caracteres}")
