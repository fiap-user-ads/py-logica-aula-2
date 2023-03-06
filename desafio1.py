"""
    DADO O PREÇO DO MAÇO DE CIGARRO, A QUANTIDADE DE MAÇOS CONSUMIDOS POR DIA E O
    TEMPO EM ANOS QUE A PESSOA FUMA, CALCULAR O QUANTO A PESSOA JÁ GASTOU FUMANDO
"""

# obter valores
preco = float(input("Digite o preço do maço: "))
quantidade = float(input("Digite a quantidade de maço consumido por dia: "))
anos = float(input("A quantos anos você fuma: "))

# calcular o total gasto
tempo = 365 * anos
quantidade = tempo * quantidade
valorTotal = quantidade * preco

# mostrar resultado
print(f"O total gasto foi de R${valorTotal}")
