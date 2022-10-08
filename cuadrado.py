
#Paradigmas de Programacion
#area maxima cuadrada en una matriz de nxn de 1's y 0's
#Licenciatura en Ciencia de la Computacion, usach
#Pedro Pablo Figueroa Cerda

#matrices de prueba (lista de sublistas de tamanio nxn (cuadrada))

M=[[0, 1, 0, 0, 0, 0, 0, 1, 0 ,0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]]


D=[[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# funcion que comprueba que los bordes del cuadrado sean 0's
# compara valores tanto como por abajo, y por arriba, siempre avanzando hacia abajo
# asumiendo que la posicion entregada es la esquina superor derecha y una posicion x e y con el fin de
# poder comprobar que las orillas sean 0's 

def compruebebordes(L, ejex, ejey, x, y):
    ctex=ejex
    ctey=ejey
    contx, conty = 0,0
    contadornegativo = 0
    if ctex == len(L[0]) - 1 or ctey == len(L) - 1: 
        return 0
    elif L[ctey][ctex] == 1:
        return 0    
    for m in range(y, ctey + 1):
        if L[m][ctex]==0: 
            conty+=1
        else: 
            contadornegativo+=1    
    for n in range(x, ctex + 1):
        if L[ctey][n]==0: 
            contx+=1 
        else: 
            contadornegativo+=1

    if contadornegativo!=0: 
        return 0            
    elif contadornegativo == 0 and contx == conty: 
        return 1
    else: 
        return 0     

# funcion que retorna el cuadrado base del cuadrado mas grande, con el fin de obtener una base para ir
# formando con la funcion bordes si son 0   

def areabaserecurrencia(L, i, j): 
    if L[i+1][j]==0 and L[i][j+1]==0 and L[i+1][j+1]==0:  
        return 4
    else: 
        return 1   

#funcion que retorna el area mas grande creada por un cuadrado base y bordes contiguos         

def areagrande(L, i, j): 
    ejex, ejey = j, i
    areabase=0
    bordes=0
    area=0
    cte=2
    aumentador = 0
    if ejey < len(L) - 2 and ejex < len(L[0]) - 2:     
        areabase = areabaserecurrencia(L, ejey, ejex)
        area=areabase 
        if areabase == 1:           
            return 1   

        elif areabase == 4 and ejex < len(L[0]) - 3 and ejey < len(L) - 3: 
                ejex=ejex + 2
                ejey=ejey + 2
                bordes = compruebebordes(L, ejex, ejey, j, i)
                area = 4
                cte=3
                while bordes == 1 and ejex <= len(L[0]) - 3 or ejey <= len(L) - 3: 
                    if bordes == 0: 
                        break 
                    else: 
                        ejex+=1
                        ejey+=1
                        cte+=1

                        bordes = compruebebordes(L, ejex, ejey, j, i)
                   
    elif ejey==len(L)-1 or ejex==len(L[0])-1:
        return 1   
    if cte > 2: 
        for r in  range(1, cte): 
            area = r + r
    return area//2        


#funcion main, donde evaluamos y guardamos el ancho del cuadrado dado por area grande
#va guardando cada vez que encuentre el ancho mas grande dentro de la matriz

def cuadrado(L):
    largoi = len(L)
    largoj = len(L[0])
    auxargrande = 1
    valori=0
    valorj=0

    for i in range(largoi):
        for j in range(largoj): 
            if L[i][j] == 0: 
                aux = areagrande(L, i, j)
                if aux > auxargrande: 
                    valori = i
                    valorj = j
                    auxargrande = aux
    return valorj, valori, auxargrande

print(cuadrado(M))

print(cuadrado(D))  

         
            









        