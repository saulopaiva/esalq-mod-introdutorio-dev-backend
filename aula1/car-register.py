def getBiggerStrings(cars):
    biggerName = 15
    biggerYear = 6

    for car in cars:
        if (len(car['nome']) > biggerName):
            biggerName = len(car['nome'])

        if (len(car['ano']) > biggerYear):
            biggerYear = len(car['ano'])
    
    return {
        'name': biggerName,
        'year': biggerYear,
        'total': biggerName + biggerYear,
    }


##############################################################
##############################################################

print('====================================')
print('        CADASTRO DE VEÍCULOS        ')
print('====================================')

cars = []
more = 's'

while more == 's':
    print('')
    nome = input('Digite o nome do veículo: ')
    ano = input('Digite o ano do veículo: ')
    more = input('Deseja cadastrar novo veículo? (s/n): ')
    cars.append({
        'nome': nome,
        'ano': ano,
    })

biggerStr = getBiggerStrings(cars)
totalSize = biggerStr['total'] + 5

print('\n')
print(f"/{'='.ljust(totalSize, '=')}\\")
print(f"|{'VEICULOS CADASTRADOS'.center(totalSize)}|")
print(f"|{'='.ljust(totalSize, '=')}|")

print(f"| {'nome'.ljust(biggerStr['name'])} | {'ano'.ljust(biggerStr['year'])} |")
print(f"|{'-'.ljust(totalSize, '-')}|")

for car in cars:
    print(f"| {car['nome'].ljust(biggerStr['name'])} | {car['ano'].ljust(biggerStr['year'])} |")

print(f"\\{'-'.ljust(totalSize, '-')}/")
