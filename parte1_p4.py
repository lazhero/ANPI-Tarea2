import parte1_p1
from parte1_p2 import jacobi
from parte1_p3 import jacobiParallel
from parte1_p1 import *
import multiprocessing


if __name__=='__main__':
    
    tol=pow(10,-5)
    iterMax=1000
    m=242
    p=q=getInicialP(m)
    A=tridiagonal(p, q, m)
    b=getInitialB(m)
    x0=getInitialX0(m)

    xa,iteraciones0,error0,elapse0=jacobi(A, x0, b, iterMax, tol)


    for i in range(1,multiprocessing.cpu_count()):
        x,iteraciones,error,elapsed=jacobiParallel(A, x0, b, iterMax,tol,i)
        aceleracion=elapse0/elapsed
        print("Aceleracion con %d nucleos es: %f" %(i,aceleracion))