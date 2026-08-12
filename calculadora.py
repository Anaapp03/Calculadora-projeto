# Calculadora (projeto)
print("Bem-vindo à Calculadora!")

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação desejada: ")

if operacao in ["1", "2", "3", "4"]:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if operacao == "1":
            resultado = numero1 + numero2
            print(f"Resultado da soma é: {resultado}")
        elif operacao == "2":
            resultado = numero1 - numero2
            print(f"Resultado da subtração é: {resultado}")
        elif operacao == "3":
            resultado = numero1 * numero2
            print(f"Resultado da multiplicação é: {resultado}")
        elif operacao == "4":
            if numero2 != 0:
                resultado = numero1 / numero2
                print(f"Resultado da divisão é: {resultado}")
            else:
                print("Não é possível dividir por 0!")  
    except ValueError:
        print("Digite apenas números válidos!")
else:
    print("Erro: opção de operação inválida.")
