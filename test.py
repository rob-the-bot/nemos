import nemos as nmo

b1 = nmo.basis.BSplineEval(5)
b2 = nmo.basis.FourierEval(5, 2)

b2.bounds = [None, (2, 3)]

print(b2.bounds)
print(b1.bounds)
a = b1 * b2
print(a.bounds)
a.evaluate_on_grid(5, 5, 5)
