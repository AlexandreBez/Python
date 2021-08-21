# entrada
print("Usuario:")
nome = input()
print("Senha:")
senha = input()

# Procesamento
if nome == "adm" and senha == "adm":
    print("Seja bem-vindo(a)", format(nome))
else:
    print("Usuario e/ou senha invalidas")
