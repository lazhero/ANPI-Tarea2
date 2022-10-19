from symbol import eval_input
from matplotlib import pyplot as plt
from math import *
import sympy as sym
def newton_rapson(Vec_ini, Vec_func, Vec_var, tol, iterMax):
    jacobianMat = calc_jacobianMat(Vec_func,Vec_var)
    xk = sym.Matrix(Vec_ini)
    err = 10000
    errors = []
    for i in range(iterMax):
        jacobianMatIter = sym.Matrix(calc_inv(Vec_func, Vec_var, xk, jacobianMat))
        xk = xk - jacobianMatIter
        fxk = sym.Matrix(eval_functionInX(Vec_func,Vec_var,xk))
        err = fxk.norm()
        errors.append(err)
        if(err < tol):
            showPlot(errors)
            return (xk, i, err)
    showPlot(errors)
    return (xk, iterMax, err)

def calc_jacobianMat(Vec_func,Vec_var):
    jacobianMat = []
    for m in Vec_func:
        jacFile = []
        for n in Vec_var:
            jacFile.append(sym.diff(m,n))
        jacobianMat.append(jacFile)
    return jacobianMat

def eval_jacobianMat(jacobianMat,Vec_ini,Vec_var):
    res = []
    for m in jacobianMat:
        res_file = []
        for n in range(len(m)):
            func=sym.lambdify(Vec_var[n], m[n],modules=["sympy"]) 
            res_file.append(func(Vec_ini[n]))
        res.append(res_file)
    return res

def eval_functionInX(Vec_func,Vec_var,Vec_ini):
    res = []
    vec_dic = formatVec_ini(Vec_ini,Vec_var)
    for m in range(len(Vec_func)):
        eval = Vec_func[m].subs(vec_dic)
        res.append(eval)
    return res

def formatVec_ini(Vec_ini,Vec_var):
    res = []
    for i in range(len(Vec_var)):
        res.append((Vec_var[i],Vec_ini[i]))
    return res

def calc_inv(func_vec, sym_vec, x0, JacMat):
    A = sym.Matrix(eval_jacobianMat(JacMat,x0,sym_vec))
    b = sym.Matrix(eval_functionInX(func_vec,sym_vec,x0))
    res = list(sym.linsolve([A,b], sym_vec))[0]
    return res

def showPlot(errors):
    for i in range(len(errors)):
        plt.plot(i,errors[i], marker="o", color="red")
    plt.show()

#func_vec = [sym.core.sympify("x**2 + y**2 + z**2 - 1"),sym.core.sympify("2*(x**2) + y**2 - 4*z"),sym.core.sympify("3*(x**2) - 4*y + z**2")]
#sym_vec = [sym.Symbol('x'),sym.Symbol('y'),sym.Symbol('z')]
#JacMat = calc_jacobianMat(func_vec, sym_vec)
#A = sym.Matrix(eval_jacobianMat(JacMat,[0.5,0.5,0.5],sym_vec))
#b = sym.Matrix(eval_functionInX(func_vec,sym_vec,[0.5,0.5,0.5]))
#res = list(sym.linsolve([A,b], sym_vec))[0]


#print(newton_rapson([0.5,0.5,0.5], func_vec, sym_vec, 10**(-6), 400))

#print(calc_inv(func_vec,sym_vec,[3,1],JacMat))
