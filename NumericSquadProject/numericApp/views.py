from django.shortcuts import render
from numericApp.methods.Interpolation.vandermonde import vandermondeAns
from numericApp.methods.Interpolation.lagrange import lagrange
from numericApp.methods.Interpolation.divideddiff import newton_interpolation
from numericApp.methods.Interpolation.spline1 import spline1Ans
from numericApp.methods.Interpolation.spline2 import spline2Ans
from numericApp.methods.Interpolation.spline3 import spline3Ans
from numericApp.methods.Roots.secant import secant

from numericApp.methods.Roots.fixedPoint import fixedPoint
from numericApp.methods.Roots.bisection import bisection
from numericApp.methods.Roots.newton import newton
from numericApp.methods.LinearEquations.crout import croutAns
from numericApp.methods.LinearEquations.cholesky import choleskyAns
from numericApp.methods.LinearEquations.jacobi import jacobi_Ans
from numericApp.methods.LinearEquations.sor import sorAns
from numericApp.methods.LinearEquations.doolittle import doolittleAns
from numericApp.methods.Roots.incrementalSearch import incrementalSearch
from numericApp.methods.Roots.falsePosition import falsePosition
from numericApp.methods.Roots.trisection import trisection
from numericApp.methods.Roots.mulRT import mulRT
from numericApp.methods.LinearEquations.seidel import seidelAns
from numericApp.methods.Roots.muller import muller
from numericApp.methods.Roots.steffensen import steffensen
from numericApp.methods.Roots.aitken import aitken
from numericApp.methods.IVP.CompoundTrapeze import CompoundTrapeze
from numericApp.methods.IVP.euler import euler
from numericApp.methods.IVP.heun import heun
from numericApp.methods.IVP.simpson13 import simpson13
from numericApp.methods.IVP.simpson38 import simpson38


from numericApp.methods.LinearEquations.lu import LUGauss
from numericApp.methods.LinearEquations.luParcial import lu_decomposition

from numericApp.methods.LinearEquations.gausSimple import gaussSimple
from numericApp.methods.LinearEquations.gausPartialPivot import gaussPartialPivot
from numericApp.methods.LinearEquations.gausTotalPivot import gaussTotalPivot

from numericApp.Exceptions.exception import CustomException
# Create your views here.
from math import sqrt

def index(request):
    return render(request, "numericApp/index.html")

def guide(request):
    return render(request, "numericApp/userGuide.html")

def notfound(request):
    return render(request, "numericApp/notfound.html")

def vandermonde_ep(request):
    if request.method == 'POST':
        try:
            X = []
            Y = []
            size = (len(request.POST) - 1)//2
            for i in range(size):
                X.append(float(request.POST["X"+str(i)]))
                Y.append(float(request.POST["Y"+str(i)]))

            matrix, coefficients, f = vandermondeAns(X, Y)
            return render(request, "numericApp/vandermonde.html", {
                "state": 1, #Carga correcta
                "coefficients":coefficients,
                "matrix":matrix,
                "f":f,
                "X":X,
                "Y":Y,
                "size":size
                })
        except :
            return render(request, "numericApp/vandermonde.html", {
                "state": 2,
                "error": "internal error"
                }) 
    else:
        return render(request, "numericApp/vandermonde.html")

def lagrange_ep(request):
    if request.method == 'POST':
        X = []
        Y = []
        size = (len(request.POST) - 1)//2
        for i in range(size):
            X.append(float(request.POST["X"+str(i)]))
            Y.append(float(request.POST["Y"+str(i)]))
        try:
            lagrange_polynoms, polynom,fullPolynom = lagrange(X, Y)
            return render(request, "numericApp/lagrange.html", {
                "state": 1, #Carga correcta
                "lPolynoms": lagrange_polynoms,
                "polynom": polynom,
                "fullPolynom": fullPolynom,
                "X":X,
                "Y":Y,
                "size":size
                })
        except :
            return render(request, "numericApp/lagrange.html", {
                "state": 2, #Carga erronea
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/lagrange.html")

def newton_interpolation_ep(request):
    if request.method == 'POST':
        try:
            X = []
            Y = []
            size = (len(request.POST) - 1)//2
            for i in range(size):
                X.append(float(request.POST["X"+str(i)]))
                Y.append(float(request.POST["Y"+str(i)]))

            DDTable, polynom, coef = newton_interpolation(X, Y)
            return render(request, "numericApp/newton-interpolation.html", {
                "state": 1, #Carga correcta
                "DDTable": DDTable,
                "polynom": polynom,
                "X":X,
                "Y":Y,
                "size":size
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/newton-interpolation.html", {
                "state": 2,
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/newton-interpolation.html")

"""def splines_ep(request):
    if request.method == 'POST':
        try:
            X = []
            Y = []
            size = (len(request.POST) - 1)//2
            for i in range(size):
                X.append(float(request.POST["X"+str(i)]))
                Y.append(float(request.POST["Y"+str(i)]))

            Y = [xd for _, xd in sorted(zip(X, Y), key=lambda pair: pair[0])]
            X.sort()

            segments1,polBySeg1 = spline1Ans(X,Y)
            segments2,polBySeg2 = spline2Ans(X,Y)
            segments3,polBySeg3 = spline3Ans(X,Y)
            return render(request, "numericApp/splines.html", {
                "state": 1, #Carga correcta
                "segments1": zip(segments1,polBySeg1),
                "segments2": zip(segments2,polBySeg2),
                "segments3": zip(segments3,polBySeg3),
                "X":X,
                "Y":Y,
                "size":size
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/splines.html", {
                "state": 2,
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/splines.html")"""

#--------------------------------------------------------------------------------------------------------------------------------

def linearSplines_ep(request):
    if request.method == 'POST':
        try:
            X = []
            Y = []
            size = (len(request.POST) - 1)//2
            for i in range(size):
                X.append(float(request.POST["X"+str(i)]))
                Y.append(float(request.POST["Y"+str(i)]))

            Y = [xd for _, xd in sorted(zip(X, Y), key=lambda pair: pair[0])]
            X.sort()

            segments1,polBySeg1 = spline1Ans(X,Y)
            return render(request, "numericApp/linearSpline.html", {
                "state": 1, #Carga correcta
                "segments1": zip(segments1,polBySeg1),
                "X":X,
                "Y":Y,
                "size":size
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/linearSpline.html", {
                "state": 2,
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/linearSpline.html")


#--------------------------------------------------------------------------------------------------------------------------------


def cuadraticSplines_ep(request):
    if request.method == 'POST':
        try:
            X = []
            Y = []
            size = (len(request.POST) - 1)//2
            for i in range(size):
                X.append(float(request.POST["X"+str(i)]))
                Y.append(float(request.POST["Y"+str(i)]))

            Y = [xd for _, xd in sorted(zip(X, Y), key=lambda pair: pair[0])]
            X.sort()
            segments2,polBySeg2 = spline2Ans(X,Y)
            
            return render(request, "numericApp/cuadraticSpline.html", {
                "state": 1, #Carga correcta
                "segments2": zip(segments2,polBySeg2),
                "X":X,
                "Y":Y,
                "size":size
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/cuadraticSpline.html", {
                "state": 2,
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/cuadraticSpline.html")


#-------------------------------------------------------------------------------------------------------------------------------


def cubicSplines_ep(request):
    if request.method == 'POST':
        try:
            X = []
            Y = []
            size = (len(request.POST) - 1)//2
            for i in range(size):
                X.append(float(request.POST["X"+str(i)]))
                Y.append(float(request.POST["Y"+str(i)]))

            Y = [xd for _, xd in sorted(zip(X, Y), key=lambda pair: pair[0])]
            X.sort()
            segments3,polBySeg3 = spline3Ans(X,Y)
            return render(request, "numericApp/cubicSpline.html", {
                "state": 1, #Carga correcta
                "segments3": zip(segments3,polBySeg3),
                "X":X,
                "Y":Y,
                "size":size
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/cubicSpline.html", {
                "state": 2,
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/cubicSpline.html")


#--------------------------------------------------------------------------------------------------------------------------------


#ROOTS METHODS
def incremental_search_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans = incrementalSearch(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['delta']),
            int(request.POST['iterations']))

            return render(request, "numericApp/incremental-search.html", {
                "state":1,
                "ans":ans,
                "equation":request.POST['equation'],
                "x0":request.POST['x0'],
                "delta":request.POST['delta'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/incremental-search.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/incremental-search.html")

def secant_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = secant(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['x1']),
            float(request.POST['tolerance']),
            int(request.POST['iterations']))

            return render(request, "numericApp/secant.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],
                "x0":request.POST['x0'],
                "x1":request.POST['x1'],
                "tolerance":request.POST['tolerance'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/secant.html", {
                "state":2,
                "error":"internal error"
                })
    else:
        return render(request, "numericApp/secant.html")


def bisection_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = bisection(float(request.POST['xi']),
            float(request.POST['xf']),
            request.POST['equation'],
            float(request.POST['tolerance']))

            return render(request, "numericApp/bisection.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],
                "xi":request.POST['xi'],
                "xf":request.POST['xf'],
                "tolerance":request.POST['tolerance']
                })
        except:
            return render(request, "numericApp/bisection.html", {
                "state":2,
                "error":"internal error",
                })
    else:
        return render(request, "numericApp/bisection.html")

def newton_roots_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = newton(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['tolerance']),
            float(request.POST['iterations']))

            return render(request, "numericApp/newton-roots.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],

                "x0":request.POST['x0'],
                "tolerance":request.POST['tolerance'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/newton-roots.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/newton-roots.html")

def false_position_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = falsePosition(request.POST['equation'],
            float(request.POST['xi']),
            float(request.POST['xf']),
            float(request.POST['tolerance']),
            int(request.POST['iterations']))

            return render(request, "numericApp/false-position.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],
                "xi":request.POST['xi'],
                "xf":request.POST['xf'],
                "tolerance":request.POST['tolerance']
                })
        except:
            return render(request, "numericApp/false-position.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/false-position.html")

def compound_trapeze_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans = CompoundTrapeze(float(request.POST['xi']),
            float(request.POST['xf']),
            request.POST['equation'],
            int(request.POST['iterations']))

            return render(request, "numericApp/CompoundTrapeze.html", {
                "state":1,
                "ans":ans,
                "equation":request.POST['equation'],
                "xi":request.POST['xi'],
                "xf":request.POST['xf']
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/CompoundTrapeze.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/CompoundTrapeze.html")

def euler_ep(request):
    if request.method == 'POST':
        # try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans = euler(float(request.POST['x0']),
            float(request.POST['y0']),
            float(request.POST['h']),
            float(request.POST['x']),
            request.POST['equation'],)

            return render(request, "numericApp/euler.html", {
                "state":1,
                "ans":ans,
                "x0":request.POST['x0'],
                "y0":request.POST['y0'],
                "h":request.POST['h'],
                "x":request.POST['x'],
                "equation":request.POST['equation'],
                })
        # except Exception as err:
        #     print(err)
        #     return render(request, "numericApp/euler.html", {
        #         "state":2,
        #         "error": "internal error",
        #         "x0":request.POST['x0'],
        #         "y0":request.POST['y0'],
        #         "h":request.POST['h'],
        #         "x":request.POST['x'],
        #         "equation":request.POST['equation'],
        #         })
    else:
        return render(request, "numericApp/euler.html")

def heun_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans = heun(float(request.POST['t']),
            float(request.POST['y']),
            float(request.POST['h']),
            float(request.POST['x']),
            request.POST['equation'],)

            return render(request, "numericApp/heun.html", {
                "state":1,
                "ans":ans,
                "x0":request.POST['t'],
                "y0":request.POST['y'],
                "h":request.POST['h'],
                "x":request.POST['x'],
                "equation":request.POST['equation']
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/heun.html", {
                "state":2,
                "error": "internal error",
                "x0":request.POST['t'],
                "y0":request.POST['y'],
                "h":request.POST['h'],
                "x":request.POST['x'],
                "equation":request.POST['equation']
                })
    else:
        return render(request, "numericApp/heun.html")

def simpson1_3_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans = simpson13(float(request.POST['left']),
            float(request.POST['right']),
            float(request.POST['n']),
            request.POST['equation'])

            return render(request, "numericApp/simpson1-3.html", {
                "state":1,
                "ans":ans,
                "left":request.POST['left'],
                "right":request.POST['right'],
                "n":request.POST['n'],
                "equation":request.POST['equation']
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/simpson1-3.html", {
                "state":2,
                "error": "internal error",
                "left":request.POST['left'],
                "right":request.POST['right'],
                "n":request.POST['n'],
                "equation":request.POST['equation']
                })
    else:
        return render(request, "numericApp/simpson1-3.html")

def simpson3_8_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans = simpson38(float(request.POST['left']),
            float(request.POST['right']),
            int(request.POST['n']),
            request.POST['equation'])

            return render(request, "numericApp/simpson3-8.html", {
                "state":1,
                "ans":ans,
                "left":request.POST['left'],
                "right":request.POST['right'],
                "n":request.POST['n'],
                "equation":request.POST['equation']
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/simpson3-8.html", {
                "state":2,
                "error": "internal error",
                "left":request.POST['left'],
                "right":request.POST['right'],
                "n":request.POST['n'],
                "equation":request.POST['equation']
                })
    else:
        return render(request, "numericApp/simpson3-8.html")

def trisection_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = trisection(request.POST['equation'],
            float(request.POST['xi']),
            float(request.POST['xf']),
            float(request.POST['tolerance']),
            float(request.POST['iterations']))

            return render(request, "numericApp/trisection.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],
                "xi":request.POST['xi'],
                "xf":request.POST['xf'],
                "tolerance":request.POST['tolerance']
                })
        except Exception as err:
            print(err)
            return render(request, "numericApp/trisection.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/trisection.html")

def mulRT_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = mulRT(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['tolerance']),
            float(request.POST['iterations']))

            return render(request, "numericApp/mulRT.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],

                "x0":request.POST['x0'],
                "tolerance":request.POST['tolerance'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/mulRT.html", {
                "state":2,
                "error": "error",
                })
    else:
        return render(request, "numericApp/mulRT.html")

def muller_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = muller(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['x1']),
            float(request.POST['tolerance']),
            float(request.POST['iterations']))

            return render(request, "numericApp/muller.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],

                "x0":request.POST['x0'],
                "x1":request.POST['x1'],
                "tolerance":request.POST['tolerance'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/muller.html", {
                "state":2,
                "error": "error",
                })
    else:
        return render(request, "numericApp/muller.html")

def steffensen_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = steffensen(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['tolerance']),
            float(request.POST['iterations']))

            return render(request, "numericApp/steffensen.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],

                "x0":request.POST['x0'],
                "tolerance":request.POST['tolerance'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/steffensen.html", {
                "state":2,
                "error": "error",
                })
    else:
        return render(request, "numericApp/steffensen.html")

def aitken_ep(request):
    if request.method == 'POST':
        try:
            if 'graph' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            ans, procedure = aitken(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['tolerance']),
            float(request.POST['iterations']))

            return render(request, "numericApp/aitken.html", {
                "state":1,
                "ans":ans,
                "procedure":procedure,
                "equation":request.POST['equation'],

                "x0":request.POST['x0'],
                "tolerance":request.POST['tolerance'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/aitken.html", {
                "state":2,
                "error": "error",
                })
    else:
        return render(request, "numericApp/aitken.html")

def fixedPoint_ep(request):
    if request.method == 'POST':
        try:
            if 'graph1' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation'],
                })
            if 'graph2' in request.POST :
                return render(request, "numericApp/index.html", {
                "equation":request.POST['equation2'],
                })
            message, matrix = fixedPoint(request.POST['equation'],
            float(request.POST['x0']),
            float(request.POST['tolerance']),
            request.POST['equation2'],
            int(request.POST['iterations']))

            return render(request, "numericApp/fixedPoint.html", {
                "state":1,
                "ans":message,
                "matrix":matrix,
                "equation":request.POST['equation'],
                "equation2":request.POST['equation2'],
                "x0":request.POST['x0'],
                "tolerance":request.POST['tolerance'],
                "iterations":request.POST['iterations']
                })
        except:
            return render(request, "numericApp/fixedPoint.html", {
                "state":2,
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/fixedPoint.html")

#LINEAR EQUATIONS
def crout_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            stages, x = croutAns(A, b)

            return render(request, "numericApp/crout.html", {
                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "stages":stages,
                "x":x
                })
        except:
            return render(request, "numericApp/crout.html", {
                "state":2,
                "error": "internal error",
                })
    else:
        return render(request, "numericApp/crout.html")


def jacobi_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = [] 
            x0 = []

            size = int(sqrt(len(request.POST)))-1
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])
                x0.append([float(request.POST["x0"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            x,Tmatrix,iterations,spectralRadious = jacobi_Ans(A,b,float(request.POST['tolerance']),x0,int(request.POST['niter']))

            return render(request, "numericApp/jacobi.html", {
                "state":1,
                "A":A,
                "b":b,
                "x0":x0,
                "size":size,
                "tolerance":request.POST['tolerance'],
                "niter":request.POST['niter'],
                "Tmatrix":Tmatrix,
                "iterations":iterations,
                "spectralRadious":spectralRadious,
                "x":x
                })
        except:
            return render(request, "numericApp/jacobi.html", {
                "state":2,
                "error":"internal error",
                })
    else:
        return render(request, "numericApp/jacobi.html")


def doolittle_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            stages, x = doolittleAns(A, b)

            return render(request, "numericApp/doolittle.html", {
                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "stages":stages,
                "x":x
                })
        except:
            return render(request, "numericApp/doolittle.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/doolittle.html")

def sor_ep(request):
    if request.method == 'POST':
        A = []
        b = [] 
        x0 = []

        size = int(sqrt(len(request.POST)))-1
        for i in range(size):
            b.append(float(request.POST["B"+str(i)]))
            x0.append(float(request.POST["x0"+str(i)]))

        for i in range(size):
            q = []
            for j in range(size):
                q.append(float(request.POST["A"+str(i)+str(j)]))
            A.append(q)
        
        x,Tmatrix,iterations,spectralRadious = sorAns(A,b,x0,float(request.POST['tolerance']),float(request.POST['w']))
        

        return render(request, "numericApp/sor.html", {
            "state":1,
            "A":A,
            "b":b,
            "x0":x0,
            "size":size,
            "tolerance":request.POST['tolerance'],
            "niter":request.POST['niter'],
            "Tmatrix":Tmatrix,
            "iterations":iterations,
            "spectralRadious":spectralRadious,
            "x":x
            })
    else:
        return render(request, "numericApp/sor.html")

def seidel_ep(request):
    if request.method == 'POST':
        A = []
        b = [] 
        x0 = []

        size = int(sqrt(len(request.POST)))-1
        for i in range(size):
            b.append(float(request.POST["B"+str(i)]))
            x0.append(float(request.POST["x0"+str(i)]))

        for i in range(size):
            q = []
            for j in range(size):
                q.append(float(request.POST["A"+str(i)+str(j)]))
            A.append(q)
        
        x,Tmatrix,iterations,spectralRadious = seidelAns(A,b,float(request.POST['tolerance']),x0,int(request.POST['niter']))

        return render(request, "numericApp/seidel.html", {
            "state":1,
            "A":A,
            "b":b,
            "x0":x0,
            "size":size,
            "tolerance":request.POST['tolerance'],
            "niter":request.POST['niter'],
            "Tmatrix":Tmatrix,
            "iterations":iterations,
            "spectralRadious":spectralRadious,
            "x":x
            })
    else:
        return render(request, "numericApp/seidel.html")

def cholesky_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            stages, x = choleskyAns(A,b)

            return render(request, "numericApp/cholesky.html", {

                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "stages":stages,
                "x":x
                })
        except:
            return render(request, "numericApp/cholesky.html", {

                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/cholesky.html")
        
def simple_LU_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            stages, x = LUGauss(A, b)

            return render(request, "numericApp/simple_LU.html", {
                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "stages":stages,
                "x":x
                })
        except:
            return render(request, "numericApp/simple_LU.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/simple_LU.html")

def partial_LU_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            stages, P, x = lu_decomposition(A, b)

            return render(request, "numericApp/partial_LU.html", {
                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "P":P,
                "stages":stages,
                "x":x
                })
        except:
            return render(request, "numericApp/partial_LU.html", {
                "state":2,
                "error": "internal error"
                })
    else:
        return render(request, "numericApp/partial_LU.html")

def gauss_simple_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            x, stages = gaussSimple(A, b)

            return render(request, "numericApp/gauss-simple.html", {
                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "stages":stages,
                "x":x
                })
        except CustomException as error_message:
            return render(request, "numericApp/gauss-simple.html", {
                "state":2,
                "error": error_message,
                "A":A,
                "b":b,
                "size":size
                })
    else:
        return render(request, "numericApp/gauss-simple.html")

def gauss_partial_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            x, stages = gaussPartialPivot(A, b)

            return render(request, "numericApp/gauss-partial.html", {
                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "stages":stages,
                "x":x
                })
        except CustomException as error_message:
            return render(request, "numericApp/gauss-partial.html", {
                "state":2,
                "error": error_message,
                "A":A,
                "b":b,
                "size":size
                })
    else:
        return render(request, "numericApp/gauss-partial.html")

def gauss_total_ep(request):
    if request.method == 'POST':
        try:
            A = []
            b = []

            size= int(sqrt(len(request.POST)))
            for i in range(size):
                b.append([float(request.POST["B"+str(i)])])

            for i in range(size):
                q = []
                for j in range(size):
                    q.append(float(request.POST["A"+str(i)+str(j)]))
                A.append(q)
            
            x, stages = gaussTotalPivot(A, b)

            return render(request, "numericApp/gauss-total.html", {
                "state":1,
                "A":A,
                "b":b,
                "size":size,
                "stages":stages,
                "x":x
                })
        except CustomException as error_message:
            return render(request, "numericApp/gauss-total.html", {
                "state":2,
                "error": error_message,
                "A":A,
                "b":b,
                "size":size
                })
    else:
        return render(request, "numericApp/gauss-total.html")

