from datetime import date
print('\033[1;35m=-'*35)
print('\033[1;32mvamos saber sobre seu alistamento militar')
ano=int(input('digite o ano em que voce nasceu \033[1;33m'))
atual=date.today().year
idade=atual-ano
if ano > atual or atual-ano > 150 :
    print('     \033[1;31mERROR(data invalida)')
    print('\033[1;35m=-'*35)
if atual-ano == 18 and atual-ano < 150:
    print('\033[1;32mcomo voce nasceu em \033[1;33m{}\033[1;32m, ja tem 18 anos.Voce deve se alistar \033[1;33mIMEDIATAMENTE'.format(ano))
elif atual- ano <= 17 and idade >= 0:
    tempo=18-idade
    print('\033[1;32mvoce não deve se alistar pois tem somente \033[1;33m{}\033[1;32m anos, voce deve se alistar somente em \033[1;33m{}\033[1;32m ano(s)'.format(idade, tempo))
elif atual-ano >= 19 and atual-ano < 150:
    tempo=idade-18
    print('\033[1;32mcomo voce nasceu em \033[1;33m{}\033[1;32m, voce já deveria tem se alistado, pois tem \033[1;33m{}\033[1;32m anos. Voce deveria ter se alistado a \033[1;33m{}\033[1;32m ano(s)'.format(ano, idade, tempo))
print('\033[1;35m=-'*35)