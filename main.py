from sympy import *
x, y, z = symbols('x y z')


def req1(fx, gx, a):
    fx = sympify(fx)
    gx = sympify(gx)
    y1 = fx+gx
    y2 = fx*gx
    y3 = fx.subs(x, gx)
    y4 = fx/gx
    dy1 = diff(y1, x)
    dy2 = diff(y2, x)
    dy3 = diff(y3, x)
    dy4 = diff(y4, x)
    return (dy1.subs(x, a), dy2.subs(x, a), dy3.subs(x, a), dy4.subs(x, a))


def req2(fxyz, a1, a2, a3):
    fxyz = sympify(fxyz)
    fx = fxyz.diff(x)
    fy = fxyz.diff(y)
    fz = fxyz.diff(z)
    fxyz0 = fxyz.subs(x, a1).subs(y, a2).subs(z, a3)
    fx0 = fx.subs(x, a1).subs(y, a2).subs(z, a3)
    fy0 = fy.subs(x, a1).subs(y, a2).subs(z, a3)
    fz0 = fz.subs(x, a1).subs(y, a2).subs(z, a3)
    Lxyz0 = fxyz0+(x-a1)*fx0+(y-a2)*fy0+(z-a3)*fz0
    return Lxyz0


def req3(wxyz, xt, yt, zt, a):
    t = Symbol('t')
    wxyz = sympify(wxyz)
    xt = sympify(xt)
    yt = sympify(yt)
    zt = sympify(zt)
    wxyz = wxyz.subs(x, xt).subs(y, yt).subs(z, zt)
    wxyzt = wxyz.diff(t)
    return wxyzt.subs(t, a)


def req4(a, b, n):
    a = sympify(a)
    b = sympify(b)
    return expand((a+b)**n)


def req5(fxy):
    fxy = sympify(fxy)
    fx = fxy.diff(x)
    fy = fxy.diff(y)
    fxx = fx.diff(x)
    fxy = fx.diff(y)
    fyy = fy.diff(y)
    fxx = lambdify((x, y), fxx)
    fxy = lambdify((x, y), fxy)
    fyy = lambdify((x, y), fyy)
    Roots = solve((fx, fy), (x, y))
    minimas = []
    maximas = []
    saddlePoints = []
    if type(Roots) != list:
        Roots = [(Roots[x], Roots[y])]
    for root in Roots:
        A = fxx(root[0], root[1])*fyy(root[0], root[1])
        A -= fxy(root[0], root[1])**2
        if A < 0:
            saddlePoints.append(root)
        else:
            if fxx(root[0], root[1]) > 0:
                minimas.append(root)
            else:
                maximas.append(root)
    return (minimas, maximas, saddlePoints)


def req6(input):
    data = input.split(",")
    x = int(data[0][1:])
    y = int(data[1])
    z = int(data[2][:-1])
    secretKey = abs(x**2-y**2-z)
    cirpherText = data[3]
    output = "".join(chr(ord(ch) ^ secretKey) for ch in list(cirpherText))
    return output


def req7(setX, setY, c):
    n = len(setX)
    sumOfX = sum(setX)
    sumOfY = sum(setY)
    sumOfXY = sum([setX[i]*setY[i] for i in range(n)])
    sumOfX2 = sum([X**2 for X in setX])
    m = (sumOfX*sumOfY-n*sumOfXY)/(sumOfX**2-n*sumOfX2)
    b = (sumOfY-m*sumOfX)/n
    return round(m*c+b, 2)


def req8(fx, n, x0, eps):
    fx = sympify(fx)
    dfx = fx.diff(x)
    xt = x0
    dfx = lambdify(x, dfx)
    while abs(dfx(xt)) >= eps:
        xt = xt-n*dfx(xt)
    return round(xt, 2)


def main():
    print(req1("x**2 + 2*x", "x**3", 1))
    print(req2("x**2 + y**2 - 2*z**2 + z*log(z)", 1, 1, 1))
    print(req3("x*y + z", "cos(t)", "sin(t)", "t", 0))
    print(req4("2*x", -3, 4))
    print(req5("x*y + 4"))
    print(req6("[1,3,2],khi*nol"))
    print(req7([-2, 0, 2], [0, 2, 3], 4))
    print(req8("x**2 + 2*sin(x)", 0.1, -5, 1e-3))


main()
