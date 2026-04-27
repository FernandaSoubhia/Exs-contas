media=float(input(' Digite a média: '))
recuperacao=input('Fez recuperação? (True/False: )')=='True'
if media >=6 or recuperacao:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')