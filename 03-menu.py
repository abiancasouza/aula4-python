def soma ():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")

def subtracao ():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")

def multiplicacao ():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")

def divisao ():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero!")
def pares ():
    limite = int(input("Digite o limite para encontrar os números pares: "))
    print("Números pares até", limite, ":")
    for i in range(0, limite + 1, 2):
        print(i, end=" ")
    print()
def impares ():
    limite = int(input("Digite o limite para encontrar os números ímpares: "))
    print("Números ímpares até", limite, ":")
    for i in range(1, limite + 1, 2):
        print(i, end=" ")
    print()
def somatorio ():
    limite = int(input("Digite o limite para calcular o somatório: "))
    resultado = sum(range(1, limite + 1))
    print(f"O somatório de 1 até {limite} é: {resultado}")  
def fatorial ():
    numero = int(input("Digite um número para calcular o fatorial: "))
    if numero < 0:
        print("Erro: Fatorial não definido para números negativos!")
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        print(f"O fatorial de {numero} é: {resultado}") 
while True:
    print("CALCULADORA")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Pares")
    print("6 - Ímpares")
    print("7 - Somatório")
    print("8 - Fatorial")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        soma()
    elif opcao == "2":
        subtracao()
    elif opcao == "3":
        multiplicacao()
    elif opcao == "4":
        divisao()
    elif opcao == "5":
        pares()
    elif opcao == "6":
        impares()
    elif opcao == "7":
        somatorio()
    elif opcao == "8":
        fatorial()
    elif opcao == "0":
        print("Saindo da calculadora...")
        break
    else:
        print("Opção inválida. Tente novamente.")