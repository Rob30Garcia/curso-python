# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profuda)

from dados import produtos
from copy import deepcopy

novos_produtos = [ {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in deepcopy(produtos)]

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")
print()

# obs.: o deepcopy foi usado para não ter alterações dos dados originais

produtos_ordenados_por_nome = sorted(deepcopy(produtos), key=lambda p: p['nome'])
print(*produtos_ordenados_por_nome, sep="\n")
print()

produtos_ordenados_por_preco = sorted(deepcopy(produtos), key=lambda p:p['preco'])
print(*produtos_ordenados_por_preco, sep="\n")
