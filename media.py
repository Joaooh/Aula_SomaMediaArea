print("----------------------------------\nCálculo da média entre três notas\n----------------------------------")
nota1 = float(input("Qual é a primeira nota? "))
nota2 = float(input("Qual é a segunda nota? "))
nota3 = float(input("Qual é a terceira nota? "))
media = (nota1 + nota2 + nota3) / 3
print("----------------------------------")
print("A média do aluno foi: {}".format("%.2f"%media) + str("."))

if media >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")