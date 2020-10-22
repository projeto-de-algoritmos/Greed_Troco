def main():
    valor = int(input('Selecione o valor do troco: '))
    moedas = {1: 5, 5: 5, 10: 5, 25: 5, 50: 5, 100: 5}
    moedas = sortDict(moedas)

def sortDict(dict):
    sort = sorted(dict, reverse=True)
    sortedDict ={}
    for item in sort:
        sortedDict[item]=dict[item]
    return sortedDict

main()