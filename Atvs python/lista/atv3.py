palavra = "COMPUTACAO"

digita = input("Informe uma palavra: ")

for letra in range(0, len(digita)):
    if digita[letra] == palavra[letra]:
        print(letra)