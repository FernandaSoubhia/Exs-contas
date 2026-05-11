#Desenvolva um algoritmo que receba duas notas de um aluno (Nota 1 e Nota 2) e sua frequência nas aulas (em porcentagem, de 0 a 100).-
#O programa deve calcular a média aritmética das duas notas.-
#Em seguida, deve determinar a situação do aluno de acordo com as seguintes regras:
#● O aluno será considerado APROVADO se a média for maior ou igual a 7 e a
#frequência for maior ou igual a 75%.-
#● O aluno estará em RECUPERAÇÃO se a média for maior ou igual a 5 e menor que
#7, e a frequência for maior ou igual a 75%.
#● O aluno será considerado REPROVADO se a média for menor que 5 ou se a
#frequência for menor que 75%.
#Ao final, o programa deve exibir:
#● A média do aluno
#● A frequência informada
#● A situação final (Aprovado, Recuperação ou Reprovado)




nota=int(input('Digite sua nota (1/2): '))
frequencia=int(input('Digite sua porcentagem de frequência nas aula: '))

media=nota+nota/2
if media >= 7 and frequencia >=75 : 
    print('Aprovado')
elif media <=6 and frequencia >=75 :
    print('Recuperação')
else :
    print('Reprovado')

print('Sua média é:', media)
print('Sua frequência é:', frequencia)