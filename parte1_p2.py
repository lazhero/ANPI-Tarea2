import numpy as np
from parte1_p1 import *
import time

def jacobi(A,x,b,iterMax,tol):
    start=time.time()
    iteraciones=0
    xk=np.ndarray.tolist(np.zeros((len(x),1)))
    error=0
    for k in range(iterMax):
        iteraciones=k+1
        for i in range(len(x)):
            xk[i][0]=calculateElement(A, b, x, i)
        x=xk
        mat=np.subtract(np.dot(A,x),b)
        error=np.linalg.norm(mat)
        if(error<tol):
            break
    end=time.time()
    elapsed=end-start
    return x,iteraciones,error,elapsed

def calculateElement(A,b,x,i):

    sumaParcial=0
    for j in range(len(A)):
        if(j!=i):
            sumaParcial+=A[i][j]*x[j][0]
    return (1/(A[i][i]))*(b[i][0]-sumaParcial)

if __name__=='__main__':
    tol=pow(10,-5)
    iterMax=1000
    m=242
    p=q=getInicialP(m)
    A=tridiagonal(p, q, m)
    b=getInitialB(m)
    x0=getInitialX0(m)
    x,iteraciones,error,elapsed=jacobi(A, x0, b, iterMax,tol)

    print("La matriz resultado es: ")
    print(x)
    print("El error es: ",error)
    print("Las iteraciones son: ",iteraciones)
    print("El tiempo transcurrido es: ",elapsed)

            
