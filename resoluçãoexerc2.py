n1=float(input('Digite sua nota 1: '))
n2=float(input('Digite sua nota 2: '))
aulasDadas=int(input('Total de aulas dadas: '))
aulasAssist=int(input('Total de aulas assistidas: '))

media=(n1+n2)/2
freq=(aulasAssist/aulasDadas)*100
situação=''

if freq<75:
    situação='Retido por frequência '
else: 
    if media<5: 
        situação='Retido por notas'
    elif media>=5 :
        situação='Recuperação'
    else: 
        situação='Aprovado'
print(f'Média: {media}\nFrequência: {freq}\nSitução: {situação}')