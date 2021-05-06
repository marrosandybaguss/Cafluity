import math
import matplotlib.pyplot as plt
from .newton_rapson import newton_rapson

def t(Tpr = 1):
	return 1/Tpr

def A1(Tpr = 1):
	return 0.06125*t(Tpr)*math.e**(-1.2*(1-t(Tpr))**2)

def A2(Tpr = 1):
	return 14.76*t(Tpr) - 9.76*t(Tpr)**2 + 4.58*t(Tpr)**3

def A3(Tpr = 1):
	return 90.7*t(Tpr) - 242.2*t(Tpr)**2 + 42.4*t(Tpr)**3

def A4(Tpr = 1):
	return 2.18 + 2.82*t(Tpr)

def func_y(y = 0.1, Tpr = 1, Ppr = 1):
	return -A1(Tpr)*Ppr + (y + y**2 + y**3 - y**4)/(1-y)**3 - A2(Tpr)*y**2 + A3(Tpr)*y**A4(Tpr)

def dev_func_y(y = 0.1, Tpr = 1, Ppr = 1):
	return ((1 + 2*y + 3*y**2 - 4*y**3)*(1-y)**3 + 3*(y + y**2 + y**3 - y**4)*(1-y)**2)/(1-y)**6 - 2*A2(Tpr)*y + A3(Tpr)*A4(Tpr)*y**(A4(Tpr)-1)

def z_factor(y = 1, Tpr = 1, Ppr = 1):
  return round((A1(Tpr)*Ppr/y),4)

def graph(Tpr = 1, Ppr = 1, e_tol = 0.3, x0 = 1):
	
	tpr = Tpr - 0.45
	tpri = []
	for i in range(0,18):
		tpri.append(tpr)
		tpr = tpr + 0.05

	x = []
	y = []
	for i in range(0,18):
		y.append([])

	ppr = Ppr - 2
	for i in range(1,120):
		x.append(ppr)

		for i in range(0,18):
			y_root = newton_rapson(e_tol, x0, tpri[i], ppr, func_y, dev_func_y)
			z = z_factor(y_root, tpri[i], ppr)
			y[i].append(z)

		ppr = ppr + 0.1
	  
	# plotting the points  
	for i in range(0,18):
		plt.plot(x, y[i])

	plt.legend(["Tpr = " + str(tpri[0]), "Tpr = " + str(tpri[1]), "Tpr = " + str(tpri[2]), "Tpr = " + str(tpri[3]), "Tpr = " + str(tpri[4]), "Tpr = " + str(tpri[5]), "Tpr = " + str(tpri[6]),  "Tpr = " + str(tpri[7]), "Tpr = " + str(tpri[8]), "Tpr = " + str(tpri[9]), "Tpr = " + str(tpri[10]), "Tpr = " + str(tpri[11]), "Tpr = " + str(tpri[12]),  "Tpr = " + str(tpri[13]), "Tpr = " + str(tpri[14]),"Tpr = " + str(tpri[15]), "Tpr = " + str(tpri[16]),  "Tpr = " + str(tpri[17])], loc='upper right', bbox_to_anchor=(1.3, 0.5, 0.5, 0.5))
	
	# naming the x axis 
	plt.xlabel('Pseudoreduced Pressure Ppr') 
	# naming the y axis 
	plt.ylabel('Compressibility Factor z') 
	  
	# giving a title to my graph 
	plt.title("Hall Yarbrough's Correlation") 
	  
	# function to show the plot 
	plt.show()