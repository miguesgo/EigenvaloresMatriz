import math
archivo = open("matriz.txt")    #Abrimos el archivo de texto
contenidoArchivo = archivo.read()   #Leemos y guardamos lo que tenga
contenidoArchivo += " " #Aniadimos un espacio de mas para que almacenene el ultimo numero de la ultima fila
print("La matriz analizada es: \n" + contenidoArchivo)  #Imprimimos lo que tenia el archivo
matriz = [[]] #definimos la matriz, la cual siempre sera cuadrada, con una fila ya incluida por defecto

#Subrutinas Algebra lineal
def vectorUnitario(vector): #Funcion que calcula el vector unitario dado un vector
    vectorUnitario = []
    suma = 0.0  #Acumulador que sumara cada uno de los numeros del vector
    for numero in vector:   #Para cada numero del vector
        suma += numero**2   #Sumamos el cuadrado de sus elementos
    norma = math.sqrt(suma) #Sacamos la norma (raiz cuadrada de la suma)
    for numero in vector:   #Para cada numero del vector
        vectorUnitario.append((1/norma)*numero) #Lo multiplicamos por la norma, y asi vamos formando el vector unitario
    return vectorUnitario   #Calcula un vector unitario

def productoPunto(vector1, vector2):
    suma = 0.0  #Vamos sumando el producto de elemento por elemento de cada vector
    elemento = 0    #Indice de posicion sobre el elemento actual
    while elemento < len(vector1):  #Mientras el inidice no rebase el tamano de la lista
        suma += vector1[elemento]*vector2[elemento] #Vamos sumando el producto de elemento por elemento
        elemento += 1   #Vamos iterando
    return suma     #Calcula el producto punto de dos vectores

def sumaVectores(vector1,vector2):  #Calcula la resta de dos vectores
    vector = [] #Creamos un vector (el cual vamos a regresar), que alamacenara la resta de los vectores correspondientes
    elemento = 0    #Indice de posicion sobre el elemento actual
    if vector1 == []:
        return vector2
    elif vector2 == []:
        return vector1
    else:
        while elemento < len(vector1):  #Mientras el inidice no rebase el tamano de la lista
            vector.append(vector1[elemento] + vector2[elemento])
            elemento += 1   #Vamos iterando
        return vector   #Regresamos la suma de dos vectores

def restaVectores(vector1,vector2):     #Calcula la resta de dos vectores
    vector = []     #Creamos un vector (el cual vamos a regresar), que alamacenara la resta de los vectores correspondientes
    elemento = 0    #Indice de posicion sobre el elemento actual
    if vector1 == []:
        return vector2
    elif vector2 == []:
        return vector1
    else:
        while elemento < len(vector1):  #Mientras el inidice no rebase el tamano de la lista
            vector.append(vector1[elemento] - vector2[elemento])
            elemento += 1   #Vamos iterando
        return vector   #Regresamos el vector resultado

def productoEscalar(escalar,vector):
    vectorResultado = []    #Es el vector resultado, el cual vamos a retornar
    for elemento in vector:#Para cada elemento del vector
        vectorResultado.append(elemento*escalar)
    return vectorResultado  #El producto escalar de una matriz por un escalar

def proyeccionVectorial(vectorU, vectorV):  #La proyeccion vectorial (de un vector V sobre uno U) nos devolvera un vector
    return productoEscalar((productoPunto(vectorU,vectorV))/(productoPunto(vectorU,vectorU)),vectorU)

def Transpuesta(matriz):    #Devuelve la transpuesta de una matriz
    matrizTranspuesta = []  #Creamos otra matriz, que almacenara los vectores columna de la matriz original como sus filas (TRANSPUESTA)
    for fila in matriz:     #Por cada fila en la matriz
        matrizTranspuesta.append([])    #Creamos un nuevo vector, lo hacemos asi, por que necesitamos saber cuantos vectores debemos crear
    for fila in matriz:     #Para cada fila de la matriz
        vectorCorrespondiente = 0   #Contador de cada vector, para saber de cual estamos hablando, lo reiniciamos cada vez, para seguir iterando entre columnas
        for numero in fila:     #Para cada numero de cada fila de la matriz
            matrizTranspuesta[vectorCorrespondiente].append(numero)     #Guardamos el numero correspondiente a la columna de la fila en el vector correspondiente
            vectorCorrespondiente += 1  #Cambiamos de vector, para que se almacene el numero de cada columna de una fila en el vector
    return matrizTranspuesta    #Retorna la transpuesta de una matriz    

def productoMatriz(matriz1,matriz2):    #Hace la multiplicacion de dos matrices, nos sirve para obtener R
    matriz = []     #Donde guardaremos cada elemento para cada vector de la matriz R, misma que se retornara
    transpuestaM2 = Transpuesta(matriz2)    #Necesitamos invertir M2
    iteradorVector = 0      #Iteramos a travez de los vectores de la matriz R
    for vectorM1 in matriz1:    #Para cada vector en matriz 1
        matriz.append([])   #Anadimos un nuevo vector a la matriz R
        for vectorM2 in transpuestaM2:  #Para cada vector en matriz 2
            nuevoElemento = productoPunto(vectorM1, vectorM2)   #Hacemos el producto punto del vector correspondiente de M1 con todos los vectores de M2 (osea calculamos el siguiente elemento del vector correspondiente de la matriz R)
            matriz[iteradorVector].append(nuevoElemento)    #Anadimos el elemento calculado al vector correspondiente de la matriz R
        iteradorVector += 1#    Cambiamos de vector de la matriz R
    return matriz

def MatrizTriangular(matriz):   #Regresa True si la matriz es "Triangular Superior", todos los numeros debajo de la diagonal principal son cero
    for i in range(1, len(matriz)):     #Comienza a analizar despues del primer renglon hasta el ultimo de la matriz
        for j in range(0, i):   #Analiza los valores que haya desde el inicio de ese renglon hasta la cantidad de numeros que haya, siendo esta cantidad igual al numero del renglon
            if((matriz[i][j] > -1e-16) and (matriz[i][j] < 1e-16)):     #Con uno que estos numeros sea diferente de cero, se regresa un FALSE
                return True
    return False    #Si todos los numeros son iguales a cero, quiere decir que la matriz es TRIANGULAR SUPERIOR

#Subrutinas del programa
def crearMatriz():      #Creamos una funcion que se encargue de crear y almacenar los datos de la matriz    
    filaCorrespondiente = 0     #El contador de cada fila, para saber de cual estamos hablando
    numero = ""     #Variable tipo string que concatena los digitos del numero
    for caracter in contenidoArchivo:#Para cada caracter contenido en el archivo
        if caracter == "\n":    #Si caracter es un salto de linea, se crea una nueva fila
            matriz[filaCorrespondiente].append(float(numero))   #Almacenamos en la fila correspondiente de la matriz el numero ya concatenado (casteado a int obviamente)
            numero = ""     #Formateamos el concatenador, para poder almacenar los siguientes numeros
            matriz.append([])   #Agregamos una nueva fila a la matriz
            filaCorrespondiente = filaCorrespondiente + 1   #nueva fila, para empezar a alamacenar los numeros ahi
        elif caracter.isspace():    #Si el caracter se trata de un espacio en blanco, terminamos de concatenar el numero
            matriz[filaCorrespondiente].append(float(numero))   #y lo almacenamos en la fila correspondiente de la matriz (casteado a int obviamente)
            numero = ""     #Formateamos el concatenador, para poder almacenar los siguientes numeros
        elif caracter.isdigit() or caracter == "." or caracter == "-":      #Si el caracter se trata de un digito
            numero += caracter      #Concatenamos los digitos hasta formar el numero

def imprimeEigenvalores(matriz):    #Nos retorna la diagonal de la matriz R, osease los valores de los Eigevalores
    Eigenvalores = []
    iteradorDiagonal = 0
    for vector in matriz:   #Para cada vector de la matriz
        Eigenvalores.append(vector[iteradorDiagonal])
        iteradorDiagonal += 1
    return Eigenvalores

#Algoritmos para calculo de Eigenvalores
def Gram_Schmidt(matriz):   #Algoritmo de Gram Schmidt, que sirve para ortonormalizar la matriz
    #1 --> Obtener los vectores de la matriz (los cuales son sus columnas)
    #Sacamos la transpuesta de la matriz dada
    vectores = Transpuesta(matriz)  #Creamos otra matriz, que almacenara los vectores columna de la matriz original como sus filas,
                                    #(la invierte), lo hacemos de esta forma, para que nos sea mas facil usar los vectores
    #2 --> Calcular la ortonormzalizacion de cada vector    
    matrizOrtonormalizada =[]   #La matriz Q pues
    vectoresOrtogonales = []    #Matriz de vectores ortogonales
    iteradorLimite = 1      #Iterados que aumenta cada vez pero al mismop tiempo es el limite para la sumatoria de las proyecciones
    sumatoria = []      #Acumulador de vectores (Acumula restas de proyecciones escalares)
    for vector in vectores:     #range(len(vectores)):
        if vector == vectores[0]:   #Si se trata del primer vector
            vectorOrtogonal = vector    #El vector ortogonal es el mismo que el primer vector            
            vectoresOrtogonales.append(vectorOrtogonal)
            vectorOrtonormalizado = vectorUnitario(vectorOrtogonal)     #Ya solo sacamos su vector unitario
            matrizOrtonormalizada.append(vectorOrtonormalizado)
            iteradorOrtogonal = 0
        else:
            iteradorOrtogonal = 0
            for iterador in range(iteradorLimite):
                proyeccion = proyeccionVectorial(vectoresOrtogonales[iteradorOrtogonal], vector)
                sumatoria = sumaVectores(proyeccion, sumatoria)
                iteradorOrtogonal += 1
            vectorOrtogonal = restaVectores(vector, sumatoria)
            vectoresOrtogonales.insert(0,vectorOrtogonal)
            sumatoria = []#Reseteamos el acumulador
            vectorOrtonormalizado = vectorUnitario(vectorOrtogonal)
            iteradorLimite += 1
            matrizOrtonormalizada.append(vectorOrtonormalizado)
    return matrizOrtonormalizada#Algoritmo de Gram Schmidt

#Ahora si el tan esperado algoritmo QR
def algoritmoQR(matriz):
    respuesta = False
    numeroIteraciones = 0 
    while not respuesta:
        matrizQ = Gram_Schmidt(matriz)      #Obtenemos Q de acuerdo al algoritmo Gram_Schmidt --> 1
        matrizR = productoMatriz(matrizQ, matriz) #TranspuestaQ
        MatIterativa = productoMatriz(matrizQ,matrizR)
        respuesta = MatrizTriangular(MatIterativa)  #¿Es cierto que la matriz es triangular superior?
        if respuesta:
            print("Los Eigenvalores son: " + str(imprimeEigenvalores(MatIterativa)))
            break
        else:
            matrizQ = Gram_Schmidt(MatIterativa)
            matrizR = productoMatriz(matrizQ, MatIterativa)
            MatIterativa = productoMatriz(matrizR,matrizQ)
            return algoritmoQR(MatIterativa)

crearMatriz()   #Creamos la matriz de acuerdo a lo escrito en el archivo -->
Gram_Schmidt(matriz)
algoritmoQR(matriz)
archivo.close()   #Cerramos el archivo