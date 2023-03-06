"""
    UM CAIXA ELETRÔNICO DISPARA CÉDULAS DE 50, 20 E 10. CONSIDERANDO QUE A QUANTIDADE
    INSERIDA PELO USUÁRIO SEJA MÚLTIPLO DE 10, EXIBA QUANTAS CÉDULAS DE CADA SÃO
    NECESSÁRIAS PARA COMPOR A QUANTIA INSERIDA PELO USUÁRIO
"""

# obter quantia
quantia = int(input("Insira a quantidade para o saque: "))

retirar50 = quantia // 50
quantia = quantia - retirar50 * 50

retirar20 = quantia // 20
quantia = quantia - retirar20 * 20

retirar10 = quantia // 10

print(f"""
-- Serão retirada:
   {retirar50} notas de 50
   {retirar20} notas de 20
   {retirar10} notas de 10
""")