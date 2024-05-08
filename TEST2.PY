summa = float(input('Айландыруу учун сумманы киргизиниз: '))
valuta_1 = input('Баштапкы валютаны киргизиңиз (USD, EUR, RUB): ')
valuta_2 = input('Максаттуу валютаны киргизиңиз (USD, EUR, RUB): ')

valuta = {'USD':88.39, 'EUR':95, 'RUB':0.96}

total = summa / valuta[valuta_2]
print(total)