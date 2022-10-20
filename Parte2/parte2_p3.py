from parte2_p2 import *
from symbol import eval_input
from matplotlib import pyplot as plt
from math import sqrt
import sympy as sym


# (a)
func_vec_a = [sym.core.sympify(
    "exp(x**2) - exp(x * (2**(1/2)))"), sym.core.sympify("x - y")]
sym_vec_a = [sym.Symbol('x'), sym.Symbol('y')]


res_a = newton_rapson([0, 0], func_vec_a, sym_vec_a, 10**(-15), 500)
print("El resultado de a es:\n")
print(res_a[0])
print("El numero de iteraciones es:\n")
print(res_a[1])
print("El error es:\n")
print(res_a[2])


print("****************************************************************************************************************\n")

# (b)
func_vec_b = [sym.core.sympify("x+exp(y)-cos(y)"),
              sym.core.sympify("3*x-y-sin(y)")]
sym_vec_b = [sym.Symbol('x'), sym.Symbol('y')]
res_b = newton_rapson([0, 0], func_vec_b, sym_vec_b, 10**(-15), 500)
print("El resultado de b es:\n")
print(res_b[0])
print("El numero de iteraciones es:\n")
print(res_b[1])
print("El error es:\n")
print(res_b[2])

print("****************************************************************************************************************\n")

# (c)
func_vec_c = [sym.core.sympify(
    "x**2 - 2*x - y + 1/2"), sym.core.sympify("x**2 + 4*(y**2) - 4")]
sym_vec_c = [sym.Symbol('x'), sym.Symbol('y')]
res_c = newton_rapson([1.9007, 0.3112], func_vec_c, sym_vec_c, 10**(-12), 3)
print("El resultado de c es:\n")
print(res_c[0])
print("El numero de iteraciones es:\n")
print(res_c[1])
print("El error es:\n")
print(res_c[2])


print("****************************************************************************************************************\n")

# (d)
func_vec_d = [sym.core.sympify("x**2 + y**2 - 1"),
              sym.core.sympify("x**2 - y**2 + 0.5")]
sym_vec_d = [sym.Symbol('x'), sym.Symbol('y')]
res_d = newton_rapson([0.5, sqrt(3)/2], func_vec_d, sym_vec_d, 10**(-12), 3)
print("El resultado de d es:\n")
print(res_d[0])
print("El numero de iteraciones es:\n")
print(res_d[1])
print("El error es:\n")
print(res_d[2])


print("****************************************************************************************************************\n")

# (e)
#func_vec = [sym.core.sympify("x**2 + y**2 + z**2 - 1"),sym.core.sympify("2*(x**2) + y**2 - 4*z"),sym.core.sympify("3*(x**2) - 4*y + z**2")]
#sym_vec = [sym.Symbol('x'),sym.Symbol('y'),sym.Symbol('z')]
#JacMat = calc_jacobianMat(func_vec, sym_vec)
#A = sym.Matrix(eval_jacobianMat(JacMat,[0.5,0.5,0.5],sym_vec))
#b = sym.Matrix(eval_functionInX(func_vec,sym_vec,[0.5,0.5,0.5]))
#res = list(sym.linsolve([A,b], sym_vec))[0]


#print(newton_rapson([0.5,0.5,0.5], func_vec, sym_vec, 10**(-6), 400))

# print(calc_inv(func_vec,sym_vec,[3,1],JacMat))

print("****************************************************************************************************************\n")

# (g)
func_vec_g = [sym.core.sympify("b*c + d*(b+c)"), sym.core.sympify("a*c* + d*(a+c)"), sym.core.sympify("a*b* + d*(a+b)"), sym.core.sympify("a*b + a*b + a*c + b*c -1")
              ]
sym_vec_g = [sym.Symbol('a'), sym.Symbol('b'), sym.Symbol('c'), sym.Symbol('d')]
res_g = newton_rapson([1, 2, 1, 2],func_vec_g, sym_vec_g, 10**(-12), 5)
print("El resultado de g es:\n")
print(res_g[0])
print("El numero de iteraciones es:\n")
print(res_g[1])
print("El error es:\n")
print(res_g[2])


print("****************************************************************************************************************\n")
