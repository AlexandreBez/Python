def dizOi():
    print('oi')


dizOi()


def soma(x=0, y=0):
    return x + y


print(soma(5))


def numeros(*args):
    print(args)


numeros()
numeros(4)
numeros(5, 5, 7, 3)


def cores(**kwargs):
    print(kwargs)


cores(um='verde', dois='amarelo', tres='cinza')
