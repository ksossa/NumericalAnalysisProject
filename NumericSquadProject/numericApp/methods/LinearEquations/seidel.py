import numpy as np
from prettytable import PrettyTable
from numpy import linalg
table = PrettyTable()

a = [[4,-1,0,3],
     [1,15.5,3,8],
     [0,-1.3,-4,1.1],
     [14,5,-2,30]
    ]
n = len(a)
iters = []
major = []
initialValues = [0,0,0,0]
totalResult = [[] for y in range(len(initialValues))]
b = [1,1,1,1]

def prettyPrint(name,matrix):
    n = len(matrix)
    table = PrettyTable()
    table.field_names = [f"{name}{i}" for i in range(n)]
    table.add_rows(matrix)
    table.add_column("",[f"{name}{i}" for i in range(n)])
    print(table)

def calculateNewSeidel(x0):
    x = []
    for i in x0:
        x.append(i) 
    for i in range(0,n):
        sumi = 0
        for j in range(0,n):
            if(j != i):
                sumi= sumi + a[i][j]*x[j]
        value = (b[i]- sumi)/a[i][i]
        x[i] = value
        totalResult[i].append(value)
    return x

def norm(x):
    return linalg.norm(x) #norm2

def minus(x1,x0):
    x = []
    for i in range(0,len(x1)):
        x.append(x1[i]-x0[i])
    return x
    
def gaussSeidel(niter,tol,x0):
    cont = 0
    dispersion = tol + 1
    matrix = []
    matrix.append([0,0] + x0)
    while(dispersion > tol and cont < niter ):
        x1 = calculateNewSeidel(x0)
        dispersion = norm (minus(x1, x0))
        x0 = x1
        cont = cont +1
        matrix.append([cont,dispersion]+x1)
    return [ matrix[-1][2+i] for i in range(len(matrix[-1])-2) ],matrix

def seidelAns(a,b,tol,x0,niter):
    x,iter= gaussSeidel(niter,tol,x0)
    

    D = np.diag((np.diag(a)))
    L = np.tril(a,-1)
    U = np.triu(a,1)
    Tmatrix = np.dot(linalg.inv(D-L), U)



    #print("T Matrix:")
    #prettyPrint("T",Tmatrix)
    
    valor1 = np.linalg.eig(Tmatrix)
    lista = []
    for i in range(len(valor1)):
        lista.append(abs(valor1[i]))
    spectralRadious = max(lista[0])
    
    #print("The spectral radius is: ")
    #print(value)
    
    return x,Tmatrix,iter,spectralRadious

# niter,tol,x0 = 100,10**-7,initialValues
# seidelAns(niter,tol,x0)
