from vpython import *
import numpy.random as npr
import numpy
ITERATIONS=100000

tgraph = graph(xtitle="x", ytitle="y", xmin=-1, ymin=-1, xmax=1, ymax=1, witdth=600, height=600)
f1 = gdots(color=color.red, radius=1)
f2 = gdots(color=color.blue, radius=1)

pigraph = graph(xtitle="iteration", ytitle="approximate value", xmin=0, ymin=3, ymax=3.5, scroll=True, xmax=10000, fast=False)
pi_curve = gcurve(color=color.red)
actual = gcurve()
pi_curve = gcurve(color=color.red)
ntotal = 0
n1 = 1

for i in range(ITERATIONS):
    rate(1000)
    r = vector(npr.uniform(-1, 1), npr.uniform(-1, 1), 0)
    if mag(r) <=1:
        n1 = n1 + 1
        f1.plot(r.x, r.y)
    else:
        f2.plot(r.x, r.y)
        pass
    ntotal = ntotal + 1
    
    actual.plot(i, numpy.pi)
    tpi = 4 * n1/ntotal
    pi_curve.plot(i, tpi)