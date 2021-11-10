# Trbalhando em python com módulos e funções
    # Analisando preços...

from utilidadescev import moeda, dado

n = dado.valida('Digite o preço: R$ ')
moeda.resumo(n, 15, 20)
