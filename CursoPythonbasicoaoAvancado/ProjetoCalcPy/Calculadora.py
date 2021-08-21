import math

print("CalcPy_1.0")
print("Qual a funcao desejada?")
print("1 = soma \n2 = fracao \n3 = divisao \n4 = multiplicacao")
escolha = input()

if escolha == '1':
    print("digite um numero")
    x = input()
    print("digite um numero")
    y = input()
    resultado = float(x) + float(y)
    print(resultado)
elif escolha == '2':
    print("digite um numero")
    x = input()
    print("digite um numero")
    y = input()
    resultado = float(x) - float(y)
    print(resultado)
elif escolha == '3':
    print("digite um numero")
    x = input()
    print("digite um numero")
    y = input()
    resultado = float(x) / float(y)
    print(resultado)
elif escolha == '4':
    print("digite um numero")
    x = input()
    print("digite um numero")
    y = input()
    resultado = float(x) * float(y)
    print(resultado)
else:
    print("Digite um numero valido")
