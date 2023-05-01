# Condicionales:
'''1_Crear una lista de números con 5 números ingresados por el usuario. Luego crea una lista 
que contenga solo los 3 últimos números de la lista original.'''
# Para cortar desde inicio hasta fin, se usa esto:
# lista[inicio:fin]
# Por ejemplo, si es cero, no es necesario que se especifique:
# lista[:2]
# También se puede cortar desde determinado lugar hasta el final:
# lista[2:]
""" a,b,c,d,e =input('Ingrese un múmero: \n->'),input('Ingrese un múmero: \n->'),input('Ingrese un múmero: \n->'),input('Ingrese un múmero: \n->'),input('Ingrese un múmero: \n->')
lista=[a,b,c,d,e]
lista_cortada = lista[2:]
print(f'La lista de los 3 últimos números queda asi: \n {lista_cortada}' ) """

# Siguiente

'''2_Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara 
si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.'''
""" nota1,nota2,nota3= int(input('Ingrese su nota: \n->')),int(input('Ingrese su nota: \n->')),int(input('Ingrese su nota: \n->'))
promedio = round((nota1+nota2+nota3)/3,2)
if promedio >= 70:
    print(f'Su promedio es de: {promedio}\nUsted ha aprobado.')
else:
    print(f'Su promedio es de: {promedio}\nUsted ha desaprobado.') """


'''3_Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio
 con descuento. El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% 
 y si la clave es 02 el descuento en del 20% (solo existen dos claves). Los datos se ingresan por consola 
 (nombre,clave y precio) ;)'''

""" nombre = input('Ingrese el nombre del artículo: \n->')
clave = int(input('Ingrese la clave del artículo: \n->'))
precio_original = float(input('Ingrese el precio original del artículo: \n->'))

if clave == 1:
    print(
        f'Detalle del producto {nombre} con precio original ${precio_original}\nEl precio final con 10% de descuento es de: ${precio_original * 0.90}\nEl descuento es: ${descuento}')
elif clave == 2:
    print(
        f'Detalle del producto {nombre} con precio original ${precio_original}\nEl precio final con 20% de descuento es de: ${precio_original * 0.80}\nEl descuento es: ${descuento}')
else:
    print('La clave no existe.') """

'''4_Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. 
Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, 
si es que corresponde. P/D: Ingresá el total por consola'''

""" total = float(input('Ingrese el total: \n->'))
if total > 1000:
    print(f'El total a pagar es de: ${round(total*0.85,2)}\nEl descuento es: ${round(total*0.15,2)}')
else:
    print(f'El total a pagar es de: ${round(total,2)}') """

'''5_Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es 
divisor de m.'''

""" num1,num2 = int(input('Ingrese un número: \n->')),int(input('Ingrese otro número: \n->'))

if num1 % num2 == 0:
    print(f'El número {num1} es divisible de {num2}')
else:
    print(f'El número {num1} no es divisible de {num2}') """

'''6_Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una
cantidad distinta.Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida 
e imprimilos.(ingresá las inversiones por consola)'''
""" 
inv1,inv2,inv3 = float(input('Ingrese su inversión: \n->')),float(input('Ingrese su inversión: \n->')),float(input('Ingrese su inversión: \n->'))
inversion_total = inv1 + inv2 + inv3
porcentaje1 = round(inv1 * 100 / inversion_total,2)
porcentaje2 = round(inv2 * 100 / inversion_total,2)
porcentaje3 = round(inv3 * 100 / inversion_total,2)
print(f'El inversor 1 aportó el {porcentaje1}%\nEl inversor 2 aportó el {porcentaje2}%\nEl inversor 3 aportó el {porcentaje3}%') """

'''7_Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los 
reste y si no que los sume.
'''
""" 
num1,num2 = int(input('Ingrese un número: \n->')),int(input('Ingrese otro número: \n->'))

if num1 > num2:
    print(f'La suma es: {num1+num2}')
elif num1 == num2:
    print(f'El producto es: {num1*num2}')
else:
    print(f'La resta es: {num2 - num1}')
 """
# Listas, tuplas y diccionarios:
'''1_Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada 
componente sea igual al cuadrado del componente original. El programa mostrara la lista resultante por pantalla.'''

""" lista=[2,3,4,5,6]
potenciados=[lista[0]**2,lista[1]**2,lista[2]**2,lista[3]**2,lista[4]**2]
print(potenciados) """

'''2_Realice una función que dada una lista de enteros L, y un número entero n(que se ingresa). Elimine de la 
lista original el elemento que sea igual a ese número dado e imprime la lista sin ese número'''

'''L = [2,3,4,5,6,7]
print(L)
n = int(input('Ingrese un número: \n->'))
if n in L:
    L.remove(n)
    print(f'Lista sin {n}: \n{L}')
    print(f'El número {n} se ha eliminado')
else:
    print(f'El número {n} no se ha eliminado porque no pertenece a la lista L')
'''
'''3_Escriba un algoritmo que permita cargar 5 números y agregarlos a una lista. Y que luego, una vez cargada,
 controle y sustituya cualquier elemento negativo por 0.'''

n1,n2,n3,n4,n5 = int(input('Ingrese un numero: \n->')),int(input('Ingrese un numero: \n->')),int(input('Ingrese un numero: \n->')),int(input('Ingrese un numero: \n->')),int(input('Ingrese un numero: \n->'))
lista = [n1,n2,n3,n4,n5]
if n1 <0 :
    indice = lista.index[n1]
    lista[indice] = 0

'''4_Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda.'''

'''5_Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud
máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.'''

'''6_Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.'''

'''7_Crea un diccionario que simula ser una Agenda Telefonica y consulta un dato con su clave'''

'''8_Escribir un programa que guarde en una variable un diccionario con 3 tipos de divisas(su nombre y el simbolo), 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

'''9_Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje: <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''

'''10_Escribir un programa que guarde en un diccionario los precios de 5 frutas distintas, pregunte al usuario por una fruta, 
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
debe mostrar un mensaje informando de ello.'''

'''11_Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar 5 artículos 
y sus precios y añadir el par al diccionario. Después se debe mostrar por pantalla la lista de la compra y el monto total'''

''''''
