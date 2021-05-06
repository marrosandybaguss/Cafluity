def Xr(xr_old = 0, Tpr = 1, Ppr = 1, func_y = 1, dev_func_y = 1):
  return xr_old - func_y(xr_old, Tpr, Ppr)/dev_func_y(xr_old, Tpr, Ppr)

def error_aprox(xr_new = 1, xr_old = 0):
  return abs((xr_new - xr_old)/xr_new) * 100

def newton_rapson(e_tol = 0.3, x0 = 0, Tpr = 1, Ppr = 1, func_y = 1, dev_func_y = 1):
  e_aprox = 100
  xr_old = x0
  iterasi = 1
  while e_aprox > e_tol:
   	xr = Xr(xr_old, Tpr, Ppr, func_y, dev_func_y)
   	e_aprox = error_aprox(xr, xr_old)
   	xr_old = xr
   	iterasi = iterasi + 1
   	if iterasi == 1000:
   		break
  return xr
