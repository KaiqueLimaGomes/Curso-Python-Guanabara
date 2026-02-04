#Desafio039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento
# O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o ano que você nasceu: '))
agora = date.today().year

if agora - ano < 18:
    print('Ainda falta {} ano(s) para você se alistar!'.format((agora - ano) - 18))
elif agora - ano == 18:
    print('Está na hora de se alistar!')
elif agora - ano > 18:
    print('Já passou {} ano(s) do tempo do seu alistamento!'.format((agora - ano) - 18))
print('\033[;30;42mExército Brasileiro, braço forte, mão amiga!\033[m')