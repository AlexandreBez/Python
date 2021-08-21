from collections import namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')
cachorro2 = namedtuple('cachorro2', ['idade', 'raca', 'nome'])

ray = cachorro2(idade=2, raca="chow-chow", nome='blablacar')
print(ray)

print(ray[0])
print(ray.nome)
