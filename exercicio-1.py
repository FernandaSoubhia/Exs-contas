#Desenvolva um algoritmo que receba três valores numéricos inteiros ou reais, representando os comprimentos dos lados de um triângulo (A, B e C).-
#O programa deve, primeiramente, verificar se os valores informados podem formar um
#triângulo. Para isso, deve-se obedecer à seguinte regra: a soma de dois lados quaisquer
#deve ser sempre maior que o terceiro lado.
#Ou seja:
#● A deve ser menor que B + C-
#● B deve ser menor que A + C-
#● C deve ser menor que A + B-
#Caso os valores NÃO formem um triângulo, o programa deve exibir a mensagem:-
#"Os valores informados não formam um triângulo."-
#Caso formem um triângulo, o programa deve classificá-lo em uma das seguintes categorias:-
#● Triângulo Equilátero: quando os três lados são iguais-
#● Triângulo Isósceles: quando dois lados são iguais e um diferente-
#● Triângulo Escaleno: quando todos os lados são diferentes-
#Ao final, exiba o tipo de triângulo correspondente.-

a = int(input("Digite o comprimento do lado A: "))
b = int(input("Digite o comprimento do lado B: "))
c = int(input("Digite o comprimento do lado C: "))
 

if (a < b + c) and (b < a + c) and (c < a + b):
    #forma um triangulo
    if a ==b and b==c : #if a==b==c: python é quase o unico a suportar este tipo de resposta
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores informados não formam um triângulo.")
#elif a!=bv and b!=c and a!=c: 
#print("Triângulo Escaleno"