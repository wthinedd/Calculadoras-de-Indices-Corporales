def calcular_IMC(peso = float, altura = float)-> float:
    return peso/(altura**2)

def calcular_porcentaje_grasa(peso = float, altura = float, edad = int, valor_genero = float)-> float:
    IMC = peso/(altura**2)
    return (1.2 * IMC) + (0.23 * edad) - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso = float, altura = float, edad = int, valor_genero = int)-> float:
    return (10 * peso) + (6.25 * altura) - (5 * edad) +  valor_genero

def calcular_calorias_en_actividad(peso = float, altura = float, edad = int, valor_genero = float, valor_actividad = float)-> float:
    TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero # Vuelvo a hacer el mismo calculo que en la funcion anterior para asi no complicarse.
    return TMB * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso = float, altura = float, edad = int, valor_genero = float)-> str:
    return (10*peso) + (6.25*altura) - (5*edad) + valor_genero # Este calculo es igual que la anterior pero dentro de 'consola_calculo_calorias_adelgazar' 
                                                               # dara otro resultado por la multiplicacion '0.85 o 0.8'

