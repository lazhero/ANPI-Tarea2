from symbol import eval_input
from matplotlib import pyplot as plt
from math import *
import sympy as sym


"""
@Definicion:
@Entradas:
-Vec_ini :valor inicial
- Vec_func:vector de la funcion
- Vec_var :vector que representa la variable
- tol : tolerancia
- iterMax: iteraciones maximas
@Salidas:
-xk :
- iterMax :
- err:
"""


def newton_rapson(Vec_ini, Vec_func, Vec_var, tol, iterMax):
    jacobianMat = calc_jacobianMat(Vec_func, Vec_var)
    xk = sym.Matrix(Vec_ini)
    err = 10000
    errors = []
    for i in range(iterMax):
        jacobianMatIter = sym.Matrix(
            calc_inv(Vec_func, Vec_var, xk, jacobianMat))
        xk = xk - jacobianMatIter
        fxk = sym.Matrix(eval_functionInX(Vec_func, Vec_var, xk))
        err = fxk.norm()
        errors.append(err)
        if(err < tol):
            showPlot(errors)
            return (xk, i, err)
    showPlot(errors)
    return (xk, iterMax, err)


"""
@Definicion:
@Entradas:
-Vec_func :vector de la funcion
-Vec_var:vector que representa la variable
@Salidas:
-jacobianMat:
"""


def calc_jacobianMat(Vec_func, Vec_var):
    jacobianMat = []
    for m in Vec_func:
        jacFile = []
        for n in Vec_var:
            jacFile.append(sym.diff(m, n))
        jacobianMat.append(jacFile)
    return jacobianMat


"""
@Definicion: Evalua la matriz jacobiana considerando la variable ingresada
@Entradas:
-jacobianMat:matriz jacobiana
-Vec_ini: valor inicial
-Vec_var:vector que representa la variable
@Salidas:
-res:
"""


def eval_jacobianMat(jacobianMat, Vec_ini, Vec_var):
    res = []
    for m in jacobianMat:
        res_file = []
        for n in range(len(m)):
            func = sym.lambdify(Vec_var[n], m[n], modules=["sympy"])
            res_file.append(func(Vec_ini[n]))
        res.append(res_file)
    return res


"""
@Definicion: Evalua la funcion considerando la variable ingresada
@Entradas:
-Vec_func:vector de la funcion
-Vec_var:vector que representa la variable
-Vec_ini: valor inicial
@Salidas:
-Funcion evaluada
"""


def eval_functionInX(Vec_func, Vec_var, Vec_ini):
    res = []
    vec_dic = formatVec_ini(Vec_ini, Vec_var)
    for m in range(len(Vec_func)):
        eval = Vec_func[m].subs(vec_dic)
        res.append(eval)
    return res


"""
@Definicion: le da formato al vector inicial
@Entradas: 
-Vec_ini:  vector inicial
-Vec_var: vector que representa la variable
@Salidas:
-res: vector con formato
"""


def formatVec_ini(Vec_ini, Vec_var):
    res = []
    for i in range(len(Vec_var)):
        res.append((Vec_var[i], Vec_ini[i]))
    return res


"""
@Definicion: Calcula la inversa de la matriz jacobiana mediante otros metodos
@Entradas:
-func_vec: vector de la funcion
-sym_vec: vector que representa la variable
-x0: valor inicial
-JacMat: matriz jacobiana
@Salidas:
-
"""


def calc_inv(func_vec, sym_vec, x0, JacMat):
    A = sym.Matrix(eval_jacobianMat(JacMat, x0, sym_vec))
    b = sym.Matrix(eval_functionInX(func_vec, sym_vec, x0))
    res = list(sym.linsolve([A, b], sym_vec))[0]
    return res


"""
@Definicion:
@Entradas:
-errors: grado de errores
@Salidas:
"""


def showPlot(errors):
    for i in range(len(errors)):
        plt.plot(i, errors[i], marker="o", color="red")
    plt.show()
