#import funciones_matematicas                *se puede importar toda la carpeta de este forma
#import funciones_matematicas as func_mat     *el as es para cambiarle el nombre a la funcion

#from funciones_matematicas import sumar     * solo importa suma
#from funciones_matematicas import sumar,restar,multiplicar     * importa mas de una funcion
from funciones_matematicas import sumar,restar,multiplicar, saludo  # tambien se puede importar variables
# esto es la importacvion de la carpeta mi paquete
from mi_paquete.factorial import calcular_factorial, frase
# importar desde sub paquetes
from mi_paquete.sub_paquete.funciones_avanzadas import contar_letras

import datetime 
from datetime import datetime

# func_mat.sumar(4,5)
# func_mat.multiplicar(4,5)
# func_mat.restar(4,5)


print(calcular_factorial(5))

print(frase)

texto = "gracias por asistir a la clase"
print(contar_letras(texto))


