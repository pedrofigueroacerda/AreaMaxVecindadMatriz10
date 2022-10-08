#Paradigmas de programacion
#area maxima rectangular en una matriz de nxn de 1's y 0's
#Licenciatura en Ciencia de la Computacion, usach
#Pedro Pablo Figueroa Cerda


#matriz de prueba

M=[[0, 1, 0, 0, 0, 0, 0, 1, 0 ,0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]]

# cantidad de 0 del eje y por el borde

def cantidadcerosejey(L, x, y): 
    contador = 0
    largo = len(L) - 1
    for i in range(y, largo + 1): 
        if L[i][x]==0: 
            contador+=1
        else: 
            break 
    if contador == 1: 
        return 0
    return contador    

# cantidad de 0 en el borde por el eje x

def cantidadcerosejex(L, x, y):
    contador = 0
    largo = len(L[0]) - 1 
    for j in range(x, largo + 1): 
        if L[y][j]==0: 
            contador+=1
        else: 
            break 
    if contador == 1: 
        return 0 
    return contador    

# para las siguientes dos funciones damos cuenta que existen dos formas de ser rectangulares
# por abajo y por la derecha, aca se crean dos funciones que van creciendo como rectangulo
# el maximo de estos estara limitado por las funciones que prosiguen, el cual decide si es mas rectangulo
# hacia la derecha o hacia abajo

#crecimiento rectangular por debajo

def areagrandebajo(L, x, y): 
    ejey = y 
    ejex = x 
    auxx = 0
    contadorejex=0
    largomasgrandey = [] 
    tuplafalsa = [0, 0]
    largoy = 0
    for i in range(ejex, len(L) - 1): 
        auxx = cantidadcerosejey(L, i, ejey)
        if L[ejey][i] == 0 and auxx > 2:
            if i < auxx and contadorejex < auxx: 
                contadorejex+=1
                if auxx < contadorejex: 
                    contadorejex=-1
                elif auxx == 0: 
                    contadorejex=-1
                elif auxx !=0: 
                    largomasgrandey.append(auxx)
        
        else: 
            break
    if largomasgrandey:     
        largoy = min(largomasgrandey)
    else: 
        largoy=0    
    tuplafalsa = [contadorejex, largoy]     
    return tuplafalsa  

#crecimiento rectangular por la derecha        

def areagrandederecha(L, x, y):
    ejey = y 
    ejex = x
    auxx = 0 
    contadorejey=0
    largomasgrandex = [] #largo mas grande en ele eje x
    tuplafalsa = [0, 0]
    largox = 0
    for i in range(ejey, len(L) - 1):
        auxx = cantidadcerosejex(L, ejex, i)
        if L[i][ejex] == 0 and auxx > 2:
            if i < auxx and contadorejey < auxx: 
                contadorejey+=1
                if auxx < contadorejey: 
                    contadorejey=-1
                elif auxx == 0: 
                    contadorejey=-1
                elif auxx != 0: 
                    largomasgrandex.append(auxx)
        
        else: 
            break
    
    if largomasgrandex:    
        largox = min(largomasgrandex)
    else: 
        largox = 0    
    tuplafalsa = [largox, contadorejey]     
    return tuplafalsa

# las siguientes funciones son para lso casos donde mi pisicion se encuentra antes de llegar
# al borde de la matriz 

#funcion para el borde superior derecho

def funcionorillasupder(L, ejex, ejey):
    maximo = len(L) - 1
    x = ejex 
    y = ejey
    contador = 0
    tuplafalsa = [0, 0]
    for n in range(y, maximo): 
        if L[n][x] == 0 and L[n][x + 1]==0: 
            contador+=1 
        else: 
            break

    if contador > 0:
        tuplafalsa = [2, contador] 
        return tuplafalsa
    elif contador == 2: 
        tuplafalsa = [2, contador - 1]
        return tuplafalsa
    else:   
        tuplafalsa = [1, 1]
        return tuplafalsa

#funcion para el borde inferior izquierdo

def funcionorillainfizq(L, ejex, ejey):
    maximo = len(L[0]) - 1
    x = ejex 
    y = ejey
    contador = 0
    tuplafalsa = [0, 0]
    if L[ejey + 1][ejex] == 0:
        for n in range(x, maximo): 
            if L[y][n] == 0 and L[y + 1][n]: 
                contador+=1 
            else: 
                break

    if contador%3==0: 
        tuplafalsa = [contador, 2]
        return tuplafalsa
    elif contador%2== 0:
        tuplafalsa = [contador - 1, 2] 
        return tuplafalsa
    else:
        tuplafalsa = [1, 1] 
        return tuplafalsa  

# funcion area grande rectangular, donde solo evalua condiciones y manda a funciones
# que se encuentran arriba

def areagranderectangulo(L, y, x): 
    ejex = x
    ejey = y
    tuplafalsa = [0, 0]
    if ejey < len(L) - 2 and ejex < len(L[0]) - 2: 
        #se evaluara cual es el eje con mas cero, para ver si es rectangulo hacia la derecha o hacia abajo
        if cantidadcerosejex(L, ejex, ejey) > cantidadcerosejey(L, ejex, ejey):
            tuplafalsa = areagrandederecha(L, ejex, ejey)
        elif cantidadcerosejex(L, ejex, ejey) < cantidadcerosejey(L, ejex, ejey): 
            tuplafalsa = areagrandebajo(L, ejey, ejey) 
        return tuplafalsa       
    #casos bordes    
    elif ejex==len(L[0]) - 2 or ejey==len(L) - 2: 
        if ejex == len(L[0]) - 2 and ejey < len(L) - 2: 
            tuplafalsa = funcionorillasupder(L, ejex, ejey)
            return tuplafalsa

        if ejey == len(L) - 2 and ejex < len(L[0]) - 2: 
            tuplafalsa = funcionorillainfizq(L, ejex, ejey)
            return tuplafalsa

        elif ejex == len(L[0]) - 2 and ejey == len(L) - 2:
            if L[ejey][ejex + 1] == 0: 
                tuplafalsa = [2, 1]
                return tuplafalsa
            elif L[ejey + 1][ejex] == 0:
                tuplafalsa = [1, 2]
                return tuplafalsa
            else: 
                tuplafalsa = [1, 1]
                return tuplafalsa    
    if ejex == len(L[0]) - 1 or ejey == len(L) - 1:
        tuplafalsa = [1, 1]       
        return tuplafalsa 
    else:
        tuplafalsa = [1, 1] 
        return tuplafalsa       
    return tuplafalsa

#funcion que recorre la matriz y evalua los lados del rectangulo mas grandes
 
def rectangulo(L):
    largoi = len(L)
    largoj = len(L[0])
    auxlargo = [0, 0]
    aux = [0, 0]
    valori=0
    valorj=0

    for i in range(largoi):
        for j in range(largoj): 
            if L[i][j] == 0:
                aux = areagranderectangulo(L, i, j)
                if aux[0] >= auxlargo[0] and aux[1] >= auxlargo[1]: 
                    valori = i
                    valorj = j
                    auxlargo = [0, 0]
                    auxlargo = aux      
    return valorj, valori, auxlargo[0], auxlargo[1]

print(rectangulo(M))

