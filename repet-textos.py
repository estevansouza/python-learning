#Vamos receber um input de string e um input numérico do usuário e repetir a string o número de vezes especificado.
texto = input("Digite um texto: ")
vezes = int(input("Digite o número de vezes que deseja repetir o texto: "))
texto_repetido = texto * vezes
print("Texto repetido:\n", texto_repetido)