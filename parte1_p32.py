import numpy as np
from initialGenerators import *
import multiprocessing
import time
global Am,bm,xm
Am=[]
bm=[]
xm=[]
def jacobiParallel(A,x,b,iterMax,tol):
    global Am,xm,bm
    Am=A
    xm=x
    bm=b
    pool=multiprocessing.Pool(processes=len(A))
    start=time.time()
    iteraciones=0
    error=0
    results=[]
    for k in range(iterMax):
        iteraciones=k+1  
        
        for result in pool.map(calculateElement,range(len(x))):
            results.append(result)
        
        x=np.transpose([results])
        xm=x
      
        if(k==1):
            print(x)
        mat=np.subtract(np.dot(A,x),b)
        error=np.linalg.norm(mat)
        if(error<tol):
            break
    end=time.time()
    elapsed=end-start
    return x,iteraciones,error,elapsed

def calculateElement(i):
    global Am,bm,xm
  
    sumaParcial=0
    for j in range(len(Am)):
        if(j!=i):
            sumaParcial+=Am[i][j]*xm[j][0]
    return (1/(Am[i][i]))*(bm[i][0]-sumaParcial)
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
