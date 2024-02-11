import calculadora_indices as calc

def ejecutar_calcular_IMC()->None:
    print()
    print('En esta funcion calcularemos tu IMC o Indice de Masa Corporal, para eso digita los siguientes datos:')
    print()
    peso = (float(input('Tu peso en kilogramos: ')))
    print()
    altura = (float(input('Tu altura en metros: '))) # Hay que recordar especificar si es en metros o en centimetros.
    print()
    IMC = calc.calcular_IMC(peso, altura)
    print('Tu IMC vendria siendo:', round(IMC, 2))
    
ejecutar_calcular_IMC()