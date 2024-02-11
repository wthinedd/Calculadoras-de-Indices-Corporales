import calculadora_indices as calc

def ejecutar_calcular_calorias_en_actividad()->None:
    print()
    print('En esta funcion se calcularan el TMB dependiendo tu actividad fisica, para eso necesitamos que ingreses los datos:')
    print()
    peso = float(input('Tu peso en kilogramos: '))
    print()
    altura = float(input('Tu altura en centimetros: '))
    print()
    edad = int(input('Tu edad en años: '))
    print()
    print('Si eres hombre el valor de tu genera sera 5, si eres mujer sera -161.')
    valor_genero = float(input('El valor de tu genero seria: '))
    print()
    valor_actividad = float(input('El valor de la actividad fisica semanal seria: '))
    print()
    
    TMBaf = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print('El TMB basado en actividad fisica vendria siendo: '+str(round(TMBaf, 2))+' cal')
    
ejecutar_calcular_calorias_en_actividad()