
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