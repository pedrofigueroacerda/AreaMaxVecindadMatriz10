#Paradigmas de programacion
#Iterador de celdas libres de una matriz de 0's y 1's
#Licenciatura en Ciencia de la Computacion, usach
#Pedro Pablo Figueroa Cerda


M=[
	[0, 1, 0, 0, 0, 0, 0, 1, 0 ,0],
	[1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
]

def upleft(i,j):											#retorna vecindad en caso sea ezquina superior izquerda
	return [[i,j+1],[i+1,j],[i+1,j+1]]

def upright(i,j):											#retorna vecindad en caso sea ezquina superior derecha
	return [[i,j-1],[i+1,j],[i+1,j-1]]

def upmiddle(i,j):
	return [[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]	#retorna vecindad en caso sea fila superior 

def downleft(i,j):											#retorna vecindad en caso sea ezquina inferior izquerda
	return [[i,j+1],[i-1,j],[i-1,j+1]]

def downright(i,j):											#retorna vecindad en caso sea ezquina inferior derecha
	return [[i,j-1],[i-1,j],[i-1,j-1]]

def downmiddle(i,j):										#retorna vecindad en caso sea fila inferior 
	return [[i,j-1],[i,j+1],[i-1,j-1],[i-1,j],[i-1,j+1]]

def isleft(i,j):											#retorna vecindad en caso sea columna izquerda
	return [[i-1,j],[i+1,j],[i-1,j+1],[i,j+1],[i+1,j+1]]

def isright(i,j):											#retorna vecindad en caso sea columna derecha
	return [[i-1,j],[i+1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]

def ismiddle(i,j):											#retorna vecindad en caso sea elemento interior de la matriz
	return [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]

def checkvecinos(A,lista):									#para lista de vecinos "lista", verifica que todos los elementos de la lista, en la matriz sean 0
	for i in range(len(lista)):
		x,y = lista[i]
		if x > len(A) or y > len(A[0]):
			return 0
		else:
			if A[x][y] == 1:
				return 0
	return 1

def siesvisto(i,j,vistos):									#verifica si la tupla (i,j), que representa una posicion en la matriz, ya fue ingresada en la lista "vistos"
	x = ((i,j))
	for a in range(len(vistos)):
		if x == vistos[a]:
			return 0
	return 1

def vecindad(A,i,j):										#para cada posible hubicacion de un elemento (i,j), dentro de la matriz, retorna la lista de coordenadas de cada elemento en su vecindad
	maxy = len(A)-1
	maxx = len(A[0])-1
	if i == 0:												#si elemento esta en primera fila
		if j == 0:											#si elemento esta en ezquina izquerda
			return upleft(i,j)
		elif j == maxx:										#si elemento esta en ezquina derecha
			return upright(i,j)
		else:												#si es del interior de la fila
			return upmiddle(i,j)
	elif i == maxy:											#si elemento esta en ultima fila
		if j == 0:
			return downleft(i,j)							#si elemento esta en ezquina izqueda
		elif j == maxx:
			return downright(i,j)							#si elemento esta en ezquina derecha
		else:
			return downmiddle(i,j)							#si elemento esta en interior de la fila
	else:
		if j == 0:											#si elemento es de la columna izquerda del todo
			return isleft(i,j)	
		elif j == maxx:										#si elemento es de la columna derecha del todo
			return isright(i,j)
		else:												#si es elemento en interior de la matriz
			return ismiddle(i,j)


def trabajo(A,i,j):
	pendientes = []												#lista de elementos por ver. se conforma por [(i,j),[vecino1,vecino2,vecino3...]] tipo de elemento, donde (i,j) es tupla de elemento que se esta analisando en el ciclo				
	vistos = []													#lista de elementos que ya entraron a lista de pendientes. se conforma por [(i,j)1,(i,j)2...] tuplas de elementos analizables
	if A[i][j] == 0:											#si primer elemento por ver es 0, iniciamos operacion
		vecinos = vecindad(A,i,j)								#creamos vecindad del primer elemento
		pendientes.append([(i,j),vecinos])						#a lista de pendientes, agregamos el primer elemento y su vecindad
		vistos.append((i,j))									#a lista de elemntos vistos, agregamos primer elemento
		while pendientes:										#mientras hayan elementos pendientes
			if checkvecinos(A,pendientes[0][1]):					#si, vecindad del elemento a verificar es libre
				for b in range(len(pendientes[0][1])):					#para cada elemento de su vecindad
					y,x = pendientes[0][1][b]							#definimos sus coordenadas
					if siesvisto(y,x,vistos):							#si elemento no ha sido agregado a lista de vistos
						vistos.append((y,x))								#agregamos a lista de vistos
						vecinos = vecindad(A,y,x)							#calculamos su vecindad
						pendientes.append([(y,x),vecinos])					#agregamos elemento y su vecindad a lista de pendientes
				yield pendientes[0][0]									#retornamos tupla del elemento
				pendientes.pop(0)										#eliminamos el elemento que estabamos verificando de lista de pendientes
			else:													#si no
				pendientes.pop(0)									#eliminamos elemento de lista de pendientes
	else:
		return 0

tups = trabajo(M,5,5)

for i in tups:
	print(i)
