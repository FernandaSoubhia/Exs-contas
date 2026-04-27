senha=input('Digite a senha:')
admin=input('É administrador? (True/False): ')=='True'
if senha== '1234' and admin:
    print('Acesso permitido')
else: 
    print('Acesso negado')

