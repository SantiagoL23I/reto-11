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