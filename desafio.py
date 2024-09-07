
print("DIGITE O NUMERO DO CODIGO:\n")
entrada = input("MENU\nCódigo [1]\nCódigo[2]\nCódigo[3]\n")

if entrada == '1':
    def pertence_fibonacci(numero):
        # Inicializando os primeiros números da sequência de Fibonacci
        a, b = 0, 1
        
        # Continuar gerando a sequência enquanto b for menor ou igual ao número
        while b <= numero:
            if b == numero:
                return f"O número {numero} pertence à sequência de Fibonacci."
            a, b = b, a + b
        
        return f"O número {numero} não pertence à sequência de Fibonacci."

    # Exemplo de uso
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    print(pertence_fibonacci(numero))


if entrada == '2':
    
    def contar_a_na_string(texto):
        # Contando a ocorrência de 'a' e 'A'
        contagem = texto.lower().count('a')
        
        if contagem > 0:
            return f"A letra 'a' aparece {contagem} vezes na string."
        else:
            return "A letra 'a' não aparece na string."

    # Exemplo de uso
    texto = input("Digite uma string para verificar a existência da letra 'a': ")
    print(contar_a_na_string(texto))

if entrada == '3':

    INDICE = 12
    SOMA = 0
    K = 1

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print("O valor final de SOMA é:", SOMA)

    

