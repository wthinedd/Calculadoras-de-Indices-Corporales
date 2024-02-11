import calculadora_indices as calc
 
def ejecutar_calcular_porcentaje_grasa()->None:
    print()
    print('En esta funcion se calculara tu %GC o Porcentaje de Grasa Corporal, para eso se necesitan los siguientes datos:')
    print()
    peso = float(input('Tu peso en kilogramos: '))
    print()
    altura = float(input('Tu altura en metros: ')) # Hay que recordar especificar si es en metros o en centimetros.
    print()
    edad = int(input('Tu edad en años: '))
    print()
    print('Si eres hombre el valor de tu genera sera 10.8, si eres mujer sera 0.') # Cuidado con confundir con el otro valor de genero (H=5, M=-161)
    valor_genero = float(input('El valor de tu genero seria: '))
    print()
    
    GC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print('Tu porcentaje de grasa vendria siendo: ' +str(round(GC, 2))+'%')
    
ejecutar_calcular_porcentaje_grasa()