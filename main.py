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
    with open("input.txt", mode="r") as f:
        lines = f.readlines()
    with open("output.txt", mode="w") as f:
        def cau1():
            line1 = lines[0]
            fx = line1.split(", ")[0]
            gx = line1.split(", ")[1]
            a = int(line1.split(", ")[2])
            f.write(str(req1(fx, gx, a))[1:-1])
            f.write("\n")
        cau1()

        def cau2():
            line2 = lines[1]
            fxyz = line2.split(", ")[0]
            a1 = int(line2.split(", ")[1])
            a2 = int(line2.split(", ")[2])
            a3 = int(line2.split(", ")[3])
            f.write(str(req2(fxyz, a1, a2, a3)))
            f.write("\n")
        cau2()

        def cau3():
            line3 = lines[2]
            wxyz = line3.split(", ")[0]
            xt = line3.split(", ")[1]
            yt = line3.split(", ")[2]
            zt = line3.split(", ")[3]
            a = int(line3.split(", ")[4])
            f.write(str(req3(wxyz, xt, yt, zt, a)))
            f.write("\n")
        cau3()

        def cau4():
            line4 = lines[3]
            a = line4.split(", ")[0]
            b = line4.split(", ")[1]
            n = int(line4.split(", ")[2])
            f.write(str(req4(a, b, n)))
            f.write("\n")
        cau4()

        def cau5():
            line5 = lines[4]
            fxy = line5[:-1]
            f.write(str(req5(fxy))[1:-1])
            f.write("\n")
        cau5()

        def cau6():
            line6 = lines[5]
            input = line6[:-1]
        #     line5 = lines[4]
        #     fxy = line5.replace('\n', '')
            f.write(req6(input))
            f.write("\n")
        cau6()

        def cau7():
            line7 = lines[6]
            data = line7.split('],')
            setX = data[0][1:].split(', ')
            setY = data[1][2:].split(', ')
            for i in range(len(setX)):
                setX[i] = float(setX[i])
                setY[i] = float(setY[i])
            c = float(data[2])
            f.write(str(req7(setX, setY, c)))
            f.write("\n")
        cau7()

        def cau8():
            line8 = lines[7]
            fx = line8.split(', ')[0]
            n = float(line8.split(', ')[1])
            x0 = float(line8.split(', ')[2])
            eps = float(line8.split(', ')[3])
            f.write(str(req8(fx, n, x0, eps)))
        cau8()


main()
