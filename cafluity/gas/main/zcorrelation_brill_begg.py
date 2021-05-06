import math
import matplotlib.pyplot as plt
from .graph import get_plot

maxTpr = 3
minTpr = 1.15
maxPpr = 15
minPpr = 0.2

def boundary_check(Tpr, Ppr):
	if Tpr < minTpr or Tpr > maxTpr:
		return 0
	
	if Ppr < minPpr or Ppr > maxPpr:
		return 0

	return 1

def z_factor(Tpr = 1, Ppr = 1):
	if boundary_check(Tpr, Ppr):

		F = 0.3106 - 0.49*Tpr + 0.1824*Tpr**2
		E = 9*(Tpr - 1)
		D = 10**F
		C = 0.132 - 0.32*math.log(Tpr, 10)
		B = (0.62 - 0.23*Tpr)*Ppr + (0.066/(Tpr - 0.86) - 0.037)*Ppr**2 + (0.32*Ppr**2)/(10**E)
		A = 1.39*(Tpr - 0.92)**0.5 - 0.36*Tpr - 0.10
		return round((A + (1 - A) / math.e**B + C*Ppr**D),4)

	else:
		return "NULL"

def multi_graph(Tpr = 1, Ppr = 1):
	
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
			z = z_factor(tpri[i], ppr)
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
	plt.title("Brill & Beggi's Correlation") 
	  
	# function to show the plot 
	plt.show()

def graph(Tpr = 1, Ppr = 1):
	if Ppr-minPpr >= 1.5:
		if Ppr+1.5 > maxPpr:
			if Ppr > maxPpr:
				ppr = Ppr
			else:
				ppr = maxPpr - 3
		else:
			ppr = Ppr - 1.5
	elif Ppr-minPpr < 1.5:
		if Ppr < minPpr:
			ppr = -3
		else:
			ppr = minPpr

	x = []
	y = []

	for i in range(1,30):
		ppr = ppr + 0.1
		z = z_factor(Tpr, ppr)
		x.append(ppr)
		y.append(z)

	title = "Brill Begg's Correlation"
	xlabel = 'Pseudoreduced Pressure Ppr'
	ylabel = 'Compressibility Factor z'

	chart = get_plot(x, y, title, xlabel, ylabel)

	return chart

