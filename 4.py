
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