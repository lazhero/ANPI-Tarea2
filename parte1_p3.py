import numpy as np
from initialGenerators import *
import multiprocessing
import time
def jacobiParallel(A,x,b,iterMax,tol):
    start=time.time()
    pool=multiprocessing.Pool()
    iteraciones=0
    error=0
    for k in range(iterMax):
        iteraciones=k+1  
        args=[(A,b,x,i) for i in range(len(x))]
        results=pool.starmap(calculateElement, args)
        x=np.transpose([results])
        if(k==1):
            print(x)
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
    m=5
    p=q=getInicialP(m)
    A=tridiagonal(p, q, m)
    b=getInitialB(m)
    x0=getInitialX0(m)
    x,iteraciones,error,elapsed=jacobiParallel(A, x0, b, iterMax,tol)

    print("La matriz resultado es: ")
    print(x)
    print("El error es: ",error)
    print("Las iteraciones son: ",iteraciones)
    print("El tiempo trancurrido es: ",elapsed)
