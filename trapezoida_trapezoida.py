import pylab
import numpy
f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = float(input('masukkan a: '))
b = float(input('masukkan b: '))
n = int(input('masukkan n: '))
h = (b-a)/n
s = 0
x = a
print("%s\t\t\t%s\t\t\t%s\t\t\t%s"%("x","fx","f(x)+h","I"))
while(True):
    if(x>b-h):
        break
    fx = f(x)
    fxh = f(x+h)
    s += h * 0.5 * (fx+fxh)
    print("%.6f\t%.6f\t%.6f\t%.6f" % (x,fx,fxh,s))
    x += h

xplot = numpy.linspace(a,b,100)
yplot = f(xplot)
pylab.plot(xplot,yplot)
pylab.show()

