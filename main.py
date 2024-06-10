from forex_python.converter import CurrencyRates

# recebe o valor da moeda a ser convertida
valor = str(input('Informe o valor a ser convertido: '))
valor = float(valor.replace(',', '.'))

moeda_orgm = input('Informe qua a moeda de origem: ').upper()
moeda_dstn = input('informa a moeda de destino: ').upper()

# faz a conversar de acrodo com a taxa de cambio
result = CurrencyRates().convert(moeda_orgm, moeda_dstn, valor)

print(f'O valor de {valor:,.2f} em {moeda_orgm} corresponde a {result:,.2f} em {moeda_dstn} ')