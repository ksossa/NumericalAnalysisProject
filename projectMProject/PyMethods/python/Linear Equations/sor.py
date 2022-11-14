import numpy as np
from prettytable import PrettyTable
from numpy import linalg

table = PrettyTable()
def prettyPrint(name,matrix):
    n = len(matrix)
    table = PrettyTable()
    table.field_names = [f"{name}{i}" for i in range(n)]
    table.add_rows(matrix)
    table.add_column("",[f"{name}{i}" for i in range(n)])
    print(table)
 
def sor(A, b, tol, w):

	n = len(A)
	Xk = [0.0]*n
	sumation = 0.0
	for i in range(n):
		if A[i][i] == 0:
			exit('Los elementos A[i][i] deben ser diferentes de 0')

	Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
	minus = lambda x, y: [x[i]-y[i] for i in range(n)]

	for j in range(n):
	 	dominancia = 0.0
	 	for i in range(n):
	 		if j != i:
	 			dominancia += abs(A[i][j])
	 	if A[i][i] < dominancia:
	 		exit('La matriz no converge')
	itera = 0
	err = None

	while(norm(minus(Xk1,Xk)) / float(norm(Xk1))) > tol:
		rowAux = [itera] + ["%.5f"%value for value in Xk] + [err] 
		table.add_row(rowAux)
		Xk[:] = Xk1[:]
		for i in range(n):
			sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
			sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))
			err=(norm(minus(Xk1,Xk)) / float(norm(Xk1)))
			Xk1[i] = (float(w)/A[i][i])*(b[i] - sumation1 - sumation2) + (1-w)*Xk[i]
		itera += 1

	return Xk1


def norm(x):
    return linalg.norm(x) #norm2


a = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
b=[1,1,1,1]
tol=1e-7
w=0.7
n = len(a)

x = sor(a,b,tol,w)
table.field_names = ["Iteracion"] + [f"x{i}" for i in range(n)]  + ["Error"]
print(table)

 
D = np.diag(np.diag(a))
L = np.tril(a,-1)
U = np.triu(a,1)


Tmatrix = np.dot(linalg.inv(D - (w*L)),((1-w)*D)+(w*U))

#print("T Matrix:")
#prettyPrint("T",Tmatrix)
 
valor1 = np.linalg.eig(Tmatrix)
lista = []
for i in range(len(valor1)):
    lista.append(abs(valor1[i]))
value = max(lista[0])
 
#print("The spectral radius is: ")
#print(value)
 
table = PrettyTable()
table.field_names = [f"x{i}" for i in range(n)]
table.add_row(x)
print("\nX:")
print(table)