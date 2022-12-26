
def decorator_imprimir(func):
    
    def imprima_parametros():
        print('CAPITAL: ')
        func()
        print('TAXA: ')
        func()
        print('TEMPO: ')
        func()
    return imprima_parametros


@decorator_imprimir
def juros_sinples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

juros_sinples(1000, 5, 6)




