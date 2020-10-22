def main():
    valor = int(input('Selecione o valor do troco: '))
    moedas = {1: 5, 5: 5, 10: 5, 25: 5, 50: 5, 100: 5}
    moedas = sortDict(moedas)
    troco(valor, moedas)



def sortDict(dict):
    ordem = sorted(dict, reverse=True)
    ordemDict ={}
    for item in ordem:
        ordemDict[item]=dict[item]
    return ordemDict

def printQtd(qtMoedas, valor, moedas):
    print('\nForam utilizadas:')
    for valorMoeda in qtMoedas:
        print('{} moeda(s) de {}'.format(qtMoedas[valorMoeda], valorMoeda))
    print('Valor a devolver: {}'.format(valor))
    print('\nSeu estoque de moedas:')
    for valorMoeda in moedas:
        print('{} moeda(s) de {}'.format(moedas[valorMoeda], valorMoeda))


def troco(valor, moedas):
    qtMoedas = {}
    for valorMoeda in moedas:
        numMoedas = valor // valorMoeda
        if numMoedas > moedas[valorMoeda]:
            numMoedas = moedas[valorMoeda]
        qtMoedas[valorMoeda]=numMoedas
        moedas[valorMoeda]-=numMoedas
        valor -= numMoedas * valorMoeda
        if valor == 0:
            printQtd(qtMoedas, valor, moedas)
            return
    printQtd(qtMoedas, valor, moedas)

main()