import calculadora_indices as calc

def ejecutar_consumo_calorias_recomendado_para_adelgazar()->None:
    print()
    print('En esta funcion veras las calorias que tendras que consumir si quieres adelgazar, para eso digita los datos:')
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
    
    calorias_adelgazar = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print('Para adelgazar es recomendado que consumas entre: '+str(round(calorias_adelgazar*0.8, 2))+' cal y '+str(round(calorias_adelgazar*0.85, 2))+' cal al dia')
    
ejecutar_consumo_calorias_recomendado_para_adelgazar()