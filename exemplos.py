# exemplo de casting
'''
valor = float(input("digite um valor:"))
dobro = valor * 2

print("O dobro do número é: ", dobro)
'''

# formatação do print
'''
nome = "Erick"
idade = 18
salario = 1800

#forma 01
print(nome, idade, salario)

#forma 02
print("Nome:", nome, "Idade:", idade, "Salario:", salario )

#forma 03 ("\n" quebra linha)
print("Nome:", nome, "\nIdade:", idade, "\nSalario:", salario )

#forma 04
print("Nome: {} Idade: {} Salario: {}".format(nome, idade, salario))

#forma 05
print("Nome: {0} Idade: {1} Salario: {2}".format(nome, idade, salario))

#forma 06
print("Nome: {n} Idade: {i} Salario: {s}".format(n = nome, i = idade, s = salario))

#forma 07 -- O MELHOR
print(f"Nome: {nome} Idade: {idade} Salario: {salario}")

#formatação adicionais
salario2 = 1800.912939
idade2 = 8

valor1 = 123.9021
valor2 = 123.1
valor3 = 12312.231
valor4 = 2

print(f"Nome: {nome} Idade: {idade2:02d} Salario: {salario2:.2f}") # int - D & float - F

print(f"Extrato : R$ {valor1:8.2f}")
print(f"Extrato : R$ {valor2:8.2f}")
print(f"Extrato : R$ {valor3:8.2f}")
print(f"Extrato : R$ {valor4:8.2f}")

print(f"""
  Extrato:
  R$ {valor1:8.2f}
  R$ {valor2:8.2f}
  R$ {valor3:8.2f}
  R$ {valor4:8.2f}
""")

margem = " " * 2
resp = input(margem + "Escolha um número")
'''
