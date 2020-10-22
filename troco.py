def main():
    valor = int(input('Selecione o valor do troco: '))
    moedas = {1: 5, 5: 5, 10: 5, 25: 5, 50: 5, 100: 5}
    editDict(moedas)
    moedas = sortDict(moedas)
    troco(valor, moedas)

def sortDict(dict):
    ordem = sorted(dict, reverse=True)
    ordemDict ={}
    for item in ordem:
        ordemDict[item]=dict[item]
    return ordemDict
    
def editDict(moedas):
    print('\nO caso teste dispõe de 5 moedas de cada valor (1, 5, 10, 25, 50, 100)')
    sOuN = input('Deseja alterar o número de moedas em estoque? (s/n) ')
    if sOuN.lower() == 's':
        for moeda in moedas:
            qtd = int(input('Quantas moedas de {} deseja ter no estoque? '.format(moeda)))
            moedas[moeda] = qtd
    else:
        return

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
    print('\nO dinheiro em seu estoque não foi suficiente para devolver o troco!')        
    printQtd(qtMoedas, valor, moedas)

main()