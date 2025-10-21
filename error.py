import numpy as np

import lmfit

np.random.seed(42)

counter = 0


def parabolic(p):
    global counter
    counter += 1
    x = float(p["x"])
    y = x**2
    print(f"x: {x:.5f}, y:{y:.5f}")
    return y


fit_params = lmfit.Parameters()
fit_params.add('x', value=-2, min=-10, max=10, vary=True)

result = lmfit.minimize(parabolic, fit_params, method="ampgo", max_nfev=100)
# result = lmfit.minimize(parabolic, fit_params, method="ampgo", max_nfev=1000000)
print(lmfit.fit_report(result))
