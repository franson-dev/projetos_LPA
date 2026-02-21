s1 = "ant"
s2 = "bat"
s3 = "cod"

# Agora,utilizandooperadores + e *, crie as saídas a seguir:
print("-" * 10)
# a. ant bat cod
print(f"{s1} {s2} {s3}")
print("-" * 10)
# b. ant ant ant ant ant ant ant ant ant ant
print((s1 + " ") * 10)
print("-" * 10)
# c. ant bat bat cod cod cod
print(f"{s1} {s2} {s2} {s3} {s3} {s3}")
print("-" * 10)
# d. batbatcod batbatcod batbatcod batbatcod batbatcod
print((s2 + s2 + s3 + " ") * 5)
print("-" * 10)
