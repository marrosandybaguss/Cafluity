import math
import matplotlib.pyplot as plt
from .newton_rapson import newton_rapson
from .graph import get_plot

A1 = 0.3265
A2 = -1.0700
A3 = -0.5339
A4 = 0.01569
A5 = -0.05165
A6 = 0.5475
A7 = -0.7361
A8 = 0.1844
A9 = 0.1056
A10 = 0.6134
A11 = 0.7210

def R1(Tpr = 1):
  return A1 + A2/Tpr + A3/Tpr**3 + A4/Tpr**4 + A5/Tpr**5

def R2(Tpr = 1, Ppr = 1):
  return 0.27*Ppr/Tpr

def R3(Tpr = 1):
  return A6 + A7/Tpr + A8/Tpr**2

def R4(Tpr = 1):
  return A9*(A7/Tpr + A8/Tpr**2)

def R5(Tpr = 1):
  return A10/Tpr**3

def func_y(y = 1, Tpr = 1, Ppr = 1):
  return R5(Tpr)*(y**2)*(1 + A11*y**2)*math.e**(-A11*y**2) + R1(Tpr)*y - R2(Tpr, Ppr)/y + R3(Tpr)*y**2 - R4(Tpr)*y**5 + 1

def dev_func_y(y = 1, Tpr = 1, Ppr = 1):
  return 2*R5(Tpr)*y*(math.e**(-A11*y**2)) - 2*A11*R5(Tpr)*(y**2)*(math.e**(-A11*y**2)) - 2*(A11**2)*R5(Tpr)*(y**4)*(math.e**(-A11*y**2)) + 4*A11*R5(Tpr)*(y**3)*(math.e**(-A11*y**2)) + R1(Tpr) + R2(Tpr, Ppr)/y**2 + 2*R3(Tpr)*y - 5*R4(Tpr)*y**4

def z_factor(y = 1, Tpr = 1, Ppr = 1):
  return round((0.27*Ppr/(y*Tpr)),4)

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
	plt.title("Drancuk & Abou Kasem's Correlation") 
	  
	# function to show the plot 
	plt.show()