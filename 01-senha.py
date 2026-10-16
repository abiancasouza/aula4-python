nome = input("Digite seu nome: ")
senha_digitada = input("Digite sua senha: ")
senha_cadastrada = "123"

while senha_digitada != senha_cadastrada:
    print("Senha incorreta! Tente novamente.")
    senha_digitada = input("Digite sua senha: ")

print(f"{nome}, bem-vindo ao Sistema!")