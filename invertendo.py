def inverter_string(string):
    # Converte a string para uma lista de caracteres
    caracteres = list(string)
    
    # Define os índices de início e fim para inverter a lista
    inicio = 0
    fim = len(caracteres) - 1
    
    # Itera sobre a lista de caracteres até que os índices se cruzem
    while inicio < fim:
        # Troca os caracteres nas posições inicio e fim
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        # Move os índices para o próximo caractere
        inicio += 1
        fim -= 1
    
    # Retorna a string invertida
    return ''.join(caracteres)

# Exemplo de uso
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
