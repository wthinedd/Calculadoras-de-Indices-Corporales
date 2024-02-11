import calculadora_indices as calc

def ejecutar_calcular_calorias_en_reposo()->None:
    print()
    print('En esta funcion se calculara cuantas calorias gastas estando en reposo, para eso se necesita que digites los siguientes datos:')
    print()
    peso = float(input('Tu peso en kilogramos: '))
    print()
    altura = float(input('Tu altura en centimetros: '))
    print()
    edad = int(input('Tu edad en años: '))
    print()
    print('Si eres hombre el valor de tu genera sera 5, si eres mujer sera -161.')
    valor_genero = int(input('El valor de tu genero seria: '))
    print()
                         
    TBM = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print('Tu TBM vendria siendo: '+str(round(TBM, 2))+' cal')
    
ejecutar_calcular_calorias_en_reposo()