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


def getInicialP(m):

    value=1
    vector=[]
    while(len(vector)<m-1):
        vector.append(value)
        value+=0.1

    return vector


def getInitialB(m):
    
    vector=[]
    while(len(vector)<m):
        vector.append(1)
    return np.ndarray.tolist(np.transpose([vector]))
def getInitialX0(m):
    return np.zeros((m,1))



