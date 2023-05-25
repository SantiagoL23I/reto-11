# reto-11
# 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
´´´pseudocode

def Matriz(filas,columnas): # primera funcion la cual se utilizara para crear las matrices.
    matriz=[] # lista de nombre matriz vacia.
    for i in range (0,filas): # para i en el rango de 0 hasta las filas que hallan
        print("ingrese los valores de la fila" + str(i)) #El usuario ingresa los valores por fila
        fila= [] # variable vacia
        for j in range(0, columnas): # para j en el rango de 0, hasta columnas 
            valor=float(input()) #entero como valor
            fila. append(valor) # el anterior entero se adiciona a la lista vacia  
        matriz.append(fila) # fila se adiciona a la matriz vacia
    return(matriz) # retorna matriz
def sumaMatrices(columnas,filas,Matri1, Matriz2): #funcion de la suma de matrices
    suma=[] #lista vacia 
    for i in range (0,filas): 
        fila=[] #  lista vacia 
        for j in range (0,columnas):
            sumador= Matri1[i][j]+ Matriz2 [i][j] #suma de matrices donde la suma i que recorrio filas y j que reccorrio columnas
            fila.append(sumador) # adiciona a la lista vacia de fila el resultado 
        suma.append(fila) # adiciona fila a la lista vacia suma ya antes declarada
    return(suma) # retorna suma


if __name__ =="__main__":
    filas=int(input( "Diga la cantidad de filas: ")) # cantidad de filas
    columnas=int(input( "Diga la cantidad de columnas: ")) # cantidad de columnas
    print( "Introduzca los valores por fila para la matriz") #valores 

    print("Matri1")
    Matri1=Matriz(columnas,filas) # Realiza la primera matriz
    for i in range(0,filas): # recorro desde 0, hasta las filas que pidio el usuario
        print(Matri1[i]) # Imprime la primera matriz

    print(" Matriz2")
    Matriz2=Matriz(columnas,filas) # Realiza la segunda matriz  
    for i in range (0,filas): # recorro desde 0, hasta las filas que pidio el usuario
        print(Matriz2[i]) # Imprime la Segunda matriz
    
    print("Matriz3")
    Matriz3=sumaMatrices(columnas,filas,Matri1, Matriz2) 
    print("La suma de las matrices es: ")
    for i in range(0,filas):
        print (Matriz3[i])
´´´
# 2.Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
´´´pseudocode

def matriz1(): #Definimos la primera matriz
    matriz1 = [] #Matriz vacía en la cual se agregaran elementos
    for i in range(filas): #Ciclo for para filas
        fila = []
        for j in range(columnas): #Ciclo for para columnas
            elemento = int(input("Ingrese el elemento de la matriz 1: ")) #Se solicita el ingreso de los elementos
            fila.append(elemento) #Se agrega elemento por elemento en cada fila de la matriz
        matriz1.append(fila) #Se agregan las filas a la matriz
    return matriz1 #Se retorna la matriz
def matriz2():#Definimos la primera matriz
    matriz2 = [] #Matriz vacía en la cual se agregaran elementos
    for i in range(filas): #Ciclo for para filas
        fila = []
        for j in range(columnas): #Ciclo for para columnas
            elemento = int(input("Ingrese el elemento de la matriz 2: ")) #Se solicita el ingreso de los elementos
            fila.append(elemento) #Se agrega elemento por elemento en cada fila de la matriz
        matriz2.append(fila) #Se agregan las filas a la matriz
    return matriz2 #Se retorna la matriz
#Definimos la función del producto de matrices
def productoMatriz(matriz1, matriz2):
    #Para realizar el producto se deben obtener los elemento de cada fila y da cada columna por aparte
    filasMatriz1 = len(matriz1)
    columnasMatriz1 = len(matriz1[0])
    filasMatriz2 = len(matriz2)
    columnasMatriz2 = len(matriz2[0])
    # Se crea unamatriz vacia en la cual se agregaran los elementos
    matrizProducto = []
    for i in range(filasMatriz1): #Ciclo for para recorrer las filas de la matriz1
        filaProducto = [] 
        for j in range(columnasMatriz2): #Ciclo for para recorrer los elementos de las columnas de la matriz 2
            producto = 0
            for k in range(columnasMatriz1): #Dentro de dicho bucle se crea otro para las columnas de la amtriz 2
                producto += matriz1[i][k] * matriz2[k][j] #Se realiza como tal la multiplicación
            filaProducto.append(producto) #Se agregan los elementos del producto a cada fila
        matrizProducto.append(filaProducto) #Se agregan las filas a la matriz
    return matrizProducto #Se retorna la función
if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de filas y columnas que tendrá la matriz
    filas = int(input("Ingrese la cantidad de filas que contendrá la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas que contendrá la matriz: "))
    #Se llaman las funciones definidas anteriormente
    matriz1 = matriz1()
    matriz2 = matriz2()
    matrizProducto = productoMatriz(matriz1, matriz2)
    #Se imprimen los resultados usando las funciones definidas, haciendo uso de un ciclo for para imprimir la matriz resultante
    print("Matriz 1: ")
    for fila in matriz1:
        print(fila)
    print("Matriz 2:")
    for fila in matriz2:
        print(fila)
    print("Producto de matrices:")
    for fila in matrizProducto:
        print(fila)
´´´
# 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
´´´pseudocode
def matriz(filas, columnas) -> list: # Se define la función para crear una matriz dando los agumentos de filas y columnas 
    matriz = []  # Se crea una lista vacía para almacenar los valores de la matriz
    for i in range(filas):  # Se itera sobre el rango de filas
        fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual
        for j in range(columnas):  # Se itera sobre el rango de columnas
           valor = float(input("Insertar valor para la posición: "))  # Se solicita ingresar un valor para la posición en la que se encuentra 
        fila.append(valor)  # Agrega el valor ingresado a la fila
        matriz.append(fila)  # Agrega la fila a la matriz
    return matriz  # Devuelve la matriz completa como una lista de listas
def matrizTr(matriz):
    filas = len(matriz)  # Se obtiene la cantidad de filas de la matriz con la función len
    columnas = len(matriz[0])  # Se obtiene la cantidad de columnas de la matriz con la función len(
    if columnas != filas:  # Verifica si las matriz tiene la misma cantidad de filas y columnas si son difenrentes no se puede realizar la matriz transpuesta 
        print("No es posible realizar la matriz transpuesta.") # se impre el mensaje si es diferente 
    else: # sino son valores distintos : 
        matrizT = []  # Se creara una lista vacía para almacenar la matriz transpuesta

        for j in range(columnas):  # Se itera sobre las columnas de la matriz 
            fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual de la matriz transpuesta
            for i in range(filas):  # Se itera sobre las filas de la matriz 
                fila.append(matriz[i][j])  # Se agrega el valor transpuesto a la fila
            matrizT.append(fila)  # Se agrega la fila a la matriz transpuesta
        return matrizT  # Se devuelve la matriz transpuesta 
if __name__ == "__main__":
    filas = int(input("Ingrese la cantidad de filas: "))  # Se solicita ingresar el numero de filas de las matrices
    columnas = int(input("Ingrese la cantidad de columnas: "))  # Se solicita ingresar el numero de  columnas de las matrices
    matriz1 = matriz(filas, columnas)  # Se crea la matriz con la función crear_matriz
    print("La matriz 1 es: " + str(matriz1))  # Se imprime la matriz 
    matrizTrans = matrizTr(matriz1) # Se crea la matriz transpuesta llmando a la función natriz transpuesta
    print("La matriz transpuesta es:", str(matrizTrans))  # Se imprime la matriz transpuesta
´´´
# 4.
´´´pseudocode 

def matriz(filas,columnas): #  funcion la cual se utilizara para crear las matrices.
    matriz=[] #  lista de nombre matriz vacia.
    for i in range (0,filas): #  i en el rango de 0 hasta las filas que halla puesto el lector realice lo siguiente.
        print("ingrese los valores de la fila" + str(i)) #ingresar los valors que quiere por fila
        fila= [] # Ingresa otra variable vacia
        for j in range(0, columnas): # j en el rango de 0, hasta columnas realice lo siguiente.
            valor=float(input()) # entero como valor
            fila. append(valor) # el anterior entero se adiciona a la lista vacia llamada fila que declaramos antes. 
        matriz.append(fila) # fila se adicione a la matriz vacia antes declarada.
    return(matriz) # retorna matriz

def sumaColumna (filas,matrizA,k):
    Columna = [] # variable llamada columna como una lista vacia
    Sumatoria = 0 # variable definida como 0 
    for x in range(0,filas): # recorrer el numero de filas puesto por el lector
        Columna.append(matrizA[x][k-1]) #  adiciona a la lista vacia (columna) x(que inicia en 0 y aumenta hasta la cantidad de filas que puso el lecto),k-1 a k se le resta 1 debido a que en python la matriz inicia en 0 
                                        # Este proceso obtendra la columna que quiere el lector ningun dato diferente a esa columna se adicionara a la lista vacia  
    for y in range(0,len(Columna)): # recorre la lista (Columna) la cual tiene los datos de la columna en una fila 
        Sumatoria = Sumatoria + Columna[y]  
    return(Sumatoria) 


if __name__ == "__main__":
    print("Introduzca los valores por filas para la matriz")
        
    print("MATRIZ A")
    filas = int(input("Especifique el numero de filas de la primera matriz: ")) # Pide la cantidad de filas
    columnas = int(input("Especifique el numero de columnas de la primera matriz: ")) # Pide la cantidad de columnas
    matrizA = matriz(filas,columnas) # Realiza la matriz en la cual llamo a la funcion crear matriz
    for i in range (0,filas): # recorre desde 0, hasta las filas que pidio el lector
        print(matrizA[i]) # Imprime la matriz
    
    k = int(input("Cual es la columna de la que quiere obtener la sumatoria: ")) # fila de la que quiere obtenenr la sumatoria
     
    Sumatoria_k = sumaColumna (filas,matrizA,k) # Llama a la funcion suma columna 
    print(Sumatoria_k) 
´´´
# 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
´´´pseudocode 

def matriz(filas,columnas):#  funcion la cual se utilizara para crear las matrices.
    matriz=[] # lista de nombre matriz vacia.
    for i in range (0,filas): # Declaro que para i en el rango de 0 hasta las filas que halla puesto el lector realice lo siguiente.
        print("ingrese los valores de la fila" + str(i)) # Debe ingresar los valores que quiere por fila
        fila= [] # Ingresa otra variable vacia
        for j in range(0, columnas): # j en el rango de 0, hasta columnas realice lo siguiente.
            valor=float(input()) # Pide un entero como valor
            fila. append(valor) # el anterior entero se adiciona a la lista vacia llamada fila que declaramos antes. 
        matriz.append(fila) # adiciona a la matriz vacia antes declarada.
    return(matriz) # retorna matriz

def sumaFilas (filas,matrizA,k): 
    lista = [] # lista vacia
    Sumatoria = 0 # agrega una vatiable con nombre sumatoria la cual vale 0
    lista = matrizA[k-1] 
    for x in range(len(lista)): # Recorre la lista la cual contiene la fila deseada
        Sumatoria = lista[x] + Sumatoria 
    return(Sumatoria) # Retorna la sumatoria
if __name__ == "__main__":
    print("Introduzca los valores por filas para la matriz")
    print("MATRIZ A")
    filas = int(input("Especifique el numero de filas de la primera matriz: ")) # Pide la cantidad de filas
    columnas = int(input("Especifique el numero de columnas de la primera matriz: ")) # Pide la cantidad de columnas
    matrizA = matriz(filas,columnas) # Realiza la matriz en la cual llamo a la funcion crear matriz
    for i in range (0,filas): # recorrw desde 0, hasta las filas que pidio el lector
        print(matrizA[i]) # Imprime la matriz
    x = int(input("Cual es la fila de la que quiere obtener la sumatoria: ")) # Pide cual la fila de la que quiere obtenenr la sumatoria
    Sumatoriax = sumaFilas (filas,matrizA,x) # Llama a la funcion de suma de filas
    print(Sumatoriax) # Imprime la Sumatoria_K la cual llamo a la funcion
´´´
