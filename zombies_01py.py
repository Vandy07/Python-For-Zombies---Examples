'''
Informar a data de nascimento do usuário.
'''
# -*- coding: utf-8 -*-
while True:
    try:
        dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')
    except ValueError:
        print ('Voce digitou o valor errado, digite novamento no valor dd/mm/aaaa')
    else:
        meses = ['janeiro', 'fevereiro', 'março','abril', 'maio', 'junho',
                'julho','agosto', 'setembro', 'outubro', 'novembro',
                'dezembro']
        print ('Voce nascesu em: ')
        print ('%s de %s de %s' %(dia, meses[int (mes) -1], ano))
        break
