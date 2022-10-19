
import numpy as np




def tridiagonal(p,q,m):
    
    p=[0]+p
    q=q+[0]
    mat=np.zeros((m,m))

    for i in range(m):
        for j in range(m):
            if i==j:
                mat[i][j]=2*p[i]+2*q[i]
            elif i-j==1:
                mat[i][j]=p[i]
            elif j-i==1:
                mat[i][j]=q[j-1]
    
    return mat


def jacobi(A,X,b,iterMax,tol):
    
    Xk=X
    error=0
    for k in range(iterMax):
        for i in range(len(A)):
            sumaParcial=0
            for j in range(len(A)):
                if(j!=i):
                   
                    sumaParcial+=A[i][j]*X[j][0]
            
            
            
            value=(1/A[i][i])*(b[i][0]-sumaParcial)
            Xk[i][0]=value
            
            
        X=Xk
        b1=b
        m=np.subtract(np.dot(A,Xk),b1)
        
        
        error=np.linalg.norm(m)
        if(error<tol):
            break
    return X,k+1,error


def getInitialVectors(m):

    value=1
    vector=[]
    while(len(vector)<m-1):
        vector.append(value)
        value+=0.1
    return vector

def getInicialB(m):
    vector=[]
    while(len(vector)<m):
        vector.append(1)
    return np.ndarray.tolist(np.transpose([vector]))


def getmatrizExample():
    mat=np.zeros((5,5))
    for i in range(5):
        for j in range(5):
            if  i==j:
                mat[i][j]=1
            if abs(i-j)==1:
                mat[i][j]=5
    return mat





m=242
p=q=getInitialVectors(m)
A=tridiagonal(p, q, m)


b=getInicialB(m)
x0=np.ndarray.tolist(np.zeros((m,1)))


x,iteraciones,error=jacobi(A, b, b, 1000, pow(10,-10))
print(b)
#print(iteraciones)
#print(x)
#print(error)
m=np.subtract(np.dot(A,x),b)
#m=np.dot(A,x)

#print(m)

