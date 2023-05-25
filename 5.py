
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