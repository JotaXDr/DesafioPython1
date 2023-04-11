texto = input("Informe uma palavra: ")
vogais = 0

for palavra in texto:
    if palavra in "aeiouAEIOU":
        vogais += 1

print("O texto", texto, "tem", vogais, "vogais.")
