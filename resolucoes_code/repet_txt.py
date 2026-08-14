# Solicita uma string e um número inteiro como entrada
texto = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro para repetição: "))

# Retorna a string repetida o número de vezes informado (com um espaço para organização)
resultado = (texto + " ") * vezes

# Exibe o resultado final
print("O texto repetido é:", resultado)
