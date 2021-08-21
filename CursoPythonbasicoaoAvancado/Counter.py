from collections import Counter

lista = [1, 1, 1, 2, 3, 4, 3, 4, 2, 5, 8, 9, 9, 45, 87, 100]

res = Counter(lista)

print(res)

texto = "asjdi uhjkl kie ednnjd ksidikopsd kmm kwmkd kmsdc kmlmkld"

palavras = texto.split()
quant = Counter(palavras)

print(quant)

print(quant.most_common(5))
