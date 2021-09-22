# Programa para cadastro de compras e análise dos produtos cadastrados


pmv = qtdprod = soma = pmil = 0
# pmv = Produto Menor Valor, qtdprod = Quantidade de Produtos, pmil = Produtos acima de R$ 1.000,00
npb = ''
# npb = Nome Produto mais Barato
while True:
    np = str(input("Nome do produto: ")).strip()
    # np = Nome do Produto
    valor = float(input("Valor do produto: R$ "))
    while valor <= 0:
        valor = float(input("Digite um valor válido: R$ "))
    qtdprod += 1
    # Soma da quantidade de produtos cadastrados
    soma += valor
    # Soma dos valores cadastrados
    if valor > 1000:
        pmil += 1
        # Contagem da quantidade de produtos que valem mais de mil reais
    if qtdprod == 1 or valor < pmv:
        pmv = valor
        npb = np
        # Registro do valor do produto mais barato e nome do produto
    continuar = str(input("Deseja registrar mais produtos [S/N]? ")).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input("Digite 'S' para registrar mais produtos"
                              " ou 'N' para encerrar o programa: ")).strip().upper()[0]
    if continuar == 'N':
        break
print(f"O total da compra foi R$ {soma:.2f}.\nTemos {pmil} produto(s) custando mais de R$ 1.000,00.\n"
      f"O produto mais barato foi {npb} que custa R$ {pmv}.")
