from collections import deque
from collections import defaultdict
from collections import Counter
from collections import namedtuple
from collections import OrderedDict

print("Quantidade palavras: ")
limite = int(input())
aux = 0


def Main():

    print("Digite qualquer palavra: ")
    valor = input()
    deq = deque(valor)

    print(deq)

    for i in deq:
        if(i == 'a'):
            print(Counter(deque(i)))
        elif(i == 'e'):
            print(Counter(deque(i)))
        elif(i == 'i'):
            print(Counter(deque(i)))
        elif(i == 'o'):
            print(Counter(deque(i)))
        elif(i == 'u'):
            print(Counter(deque(i)))


while aux < limite:
    Main()
    aux += 1
