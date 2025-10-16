import lmfit

def parabolic(p):
  x = float(p["x"])
  y = x**2
  print (f"x: {x:.5f}, y:{y:.5f}")
  return y

fit_params = lmfit.Parameters()
fit_params.add('x', value=-2, min=-10, max=10, vary=True)

result = lmfit.minimize(parabolic, fit_params, method="ampgo", max_nfev=100)
#result = lmfit.minimize(parabolic, fit_params, method="ampgo", max_nfev=1000000)
print(lmfit.fit_report(result))

# Mejor error alcanzado (raíz del chi-cuadrado)
best_error = result.chisqr ** 0.5
print(f"Best error: {best_error}")

#print(lmfit.__version__)