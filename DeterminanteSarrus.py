# MatrizA(de Coeficientes),Matrizb(términos independientes)
# MatrizAx(Matriz de coeficientes con los terminos independientes en la primera columna)
# MatrizAy(Matriz de coeficientes con los terminos independientes en la segunda columna)
# MatrizAz(Matriz de coeficientes con los terminos independientes en la tercera columna)
# detA(determinante por Sarrus de la MatrizA)
# detAx(Determinante por Sarrus de la matriz de coeficientes con los terminos independientes en la primera columna)  
# detAy(Determinante por Sarrus de la matriz de coeficientes con los terminos independientes en la segunda columna)
# detAz(Determinante por Sarrus de la matriz de coeficientes con los terminos independientes en la tercera columna)
matriza = float()
matrizb = float()
matrizax = float()
matrizay = float()
matrizaz = float()
deta = float()
detax = float()
detay = float()
detaz = float()
# Variables de solución
solx = float()
soly = float()
solz = float()
# Posición de los términos de la MatrizA y de la Matrizb
# N(Cantidad de ecuaciones y variables del sistema lineal)
fila = int()
columna = int()
n = int()
# Cantidad de ecuaciones y variables del sistema lineal";
n = 3
# Creación de las matrices
matriza = [[float() for ind0 in range(n)] for ind1 in range(n)]
matrizb = [[float() for ind0 in range(1)] for ind1 in range(n)]
matrizax = [[float() for ind0 in range(n)] for ind1 in range(n)]
matrizay = [[float() for ind0 in range(n)] for ind1 in range(n)]
matrizaz = [[float() for ind0 in range(n)] for ind1 in range(n)]
# Almacenamiento en la MatrizA de Coeficientes
for fila in range(n):
	for columna in range(n):
		print("Digite el Coeficiente de la matriz de la posición: ",fila,",",columna)
		matriza[fila][columna] = float(input())
# Almacenamiento en la Matrizb de termninos independientes
for fila in range(n):
	print("Digite el término independiente de la posición: ",fila,",0")
	matrizb[fila][0] = float(input())
# Ver la MatrizA almacenada
print("La matriz de Coeficientes A almacenada es: ")
for fila in range(n):
	for columna in range(n):
		print(matriza[fila][columna])
# Ver la Matrizb almacenada
print("La matriz de términos independientes b almacenada es: ")
for fila in range(n):
	print(matrizb[fila][0])
# Almacenamiento de los coeficientes y terminos independientes en la MatrizAx
for fila in range(n):
	for columna in range(n):
		if columna==0:
			matrizax[fila][columna] = matrizb[fila][0]
		else:
			matrizax[fila][columna] = matriza[fila][columna]
# Ver la MatrizAx almacenada
print("La matriz de Coeficientes y terminos independientes Ax almacenada es: ")
for fila in range(n):
	for columna in range(n):
		print(matrizax[fila][columna])
# Almacenamiento de los coeficientes y terminos independientes en la MatrizAy
for fila in range(n):
	for columna in range(n):
		if columna==1:
			matrizay[fila][columna] = matrizb[fila][0]
		else:
			matrizay[fila][columna] = matriza[fila][columna]
# Ver la MatrizAy almacenada
print("La matriz de Coeficientes y terminos independientes Ay almacenada es: ")
for fila in range(n):
	for columna in range(n):
		print(matrizay[fila][columna])
# Almacenamiento de los coeficientes y terminos independientes en la MatrizAz
for fila in range(n):
	for columna in range(n):
		if columna==2:
			matrizaz[fila][columna] = matrizb[fila][0]
		else:
			matrizaz[fila][columna] = matriza[fila][columna]
# Ver la MatrizAz almacenada
print("La matriz de Coeficientes y terminos independientes Az almacenada es: ")
for fila in range(n):
	for columna in range(n):
		print(matrizaz[fila][columna])
# Cálculo del determinante de la MatrizA
print("El determinante de la matriz de Coeficientes A por Sarrus")
deta = (matriza[0][0]*matriza[1][1]*matriza[2][2])+(matriza[1][0]*matriza[2][1]*matriza[0][2])+(matriza[2][0]*matriza[0][1]*matriza[1][2])-((matriza[0][2]*matriza[1][1]*matriza[2][0])+(matriza[1][2]*matriza[2][1]*matriza[0][0])+(matriza[2][2]*matriza[0][1]*matriza[1][0]))
print("es: ",deta)
# Cálculo del determinante de la MatrizAx
print("El determinante de la matriz de Coeficientes y terminos independientes Ax por Sarrus")
detax = (matrizax[0][0]*matrizax[1][1]*matrizax[2][2])+(matrizax[1][0]*matrizax[2][1]*matrizax[0][2])+(matrizax[2][0]*matrizax[0][1]*matrizax[1][2])-((matrizax[0][2]*matrizax[1][1]*matrizax[2][0])+(matrizax[1][2]*matrizax[2][1]*matrizax[0][0])+(matrizax[2][2]*matrizax[0][1]*matrizax[1][0]))
print("es: ",detax)
# Cálculo del determinante de la MatrizAy
print("El determinante de la matriz de Coeficientes y terminos independientes Ay por Sarrus")
detay = (matrizay[0][0]*matrizay[1][1]*matrizay[2][2])+(matrizay[1][0]*matrizay[2][1]*matrizay[0][2])+(matrizay[2][0]*matrizay[0][1]*matrizay[1][2])-((matrizay[0][2]*matrizay[1][1]*matrizay[2][0])+(matrizay[1][2]*matrizay[2][1]*matrizay[0][0])+(matrizay[2][2]*matrizay[0][1]*matrizay[1][0]))
print("es: ",detay)
# Cálculo del determinante de la MatrizAz
print("El determinante de la matriz de Coeficientes y terminos independientes Az por Sarrus")
detaz = (matrizaz[0][0]*matrizaz[1][1]*matrizaz[2][2])+(matrizaz[1][0]*matrizaz[2][1]*matrizaz[0][2])+(matrizaz[2][0]*matrizaz[0][1]*matrizaz[1][2])-((matrizaz[0][2]*matrizaz[1][1]*matrizaz[2][0])+(matrizaz[1][2]*matrizaz[2][1]*matrizaz[0][0])+(matrizaz[2][2]*matrizaz[0][1]*matrizaz[1][0]))
print("es: ",detaz)
# Solucion del modelo lineal 3x3 por el método del determinante
solx = detax/deta
soly = detay/deta
solz = detaz/deta
print("La solución de la variable x del sistema es: ",solx)
print("La solución de la variable y del sistema es: ",soly)
print("La solución de la variable z del sistema es: ",solz)