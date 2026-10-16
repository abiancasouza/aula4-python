nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))
nota_dois = float(input("Digite outra nota: "))

while True:
        resposta = input("Deseja inserir outra nota? (sim/não): ").strip().lower()
        if resposta == "sim":
                nova = float(input("Digite outra nota: "))
                nota.append(nova)
        elif resposta == "não":
                break
        else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")

nota_final = sum("notas") / len("notas")
print(f"{nome}, sua nota final é: {nota_final}")