"""
cannot be used to evaluate the derivative of the zfactor 
with respect to the pseudo-reduced pressure at Ppr = 3
"""

import math
import matplotlib.pyplot as plt
from .graph import get_plot

maxTpr = 3
minTpr = 1.15
maxPpr = 15
minPpr = 0.2
noPpr = 3

def boundary_check(Tpr, Ppr):
	if Tpr < minTpr or Tpr > maxTpr:
		return 0
	
	if Ppr < minPpr or Ppr > maxPpr:
		return 0

	if Ppr == noPpr:
		return 0

	return 1

def constants(Ppr = 1):
	if Ppr <= 3:
		A1 = 2.827793
		A2 = -0.4688191
		A3 = -1.262288
		A4 = -1.536524
		A5 = -4.535045
		A6 = 0.06895104
		A7 = 0.1903869
		A8 = 0.6200089
		A9 = 1.838479
		A10 = 0.4052367
		A11 = 1.073574
	else:
		A1 = 3.252838
		A2 = -0.1306424
		A3 = -0.6449194
		A4 = -1.518028
		A5 = -5.391019
		A6 = -0.01379588
		A7 = 0.06600633
		A8 = 0.6120783
		A9 = 2.317431
		A10 = 0.1632223
		A11 = 0.5660595

	return A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11

def z_factor(Tpr = 1, Ppr = 1):
	if boundary_check(Tpr, Ppr):
		A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11 = constants(Ppr)
		A = A1 + A3*math.log(Ppr) + A5/Tpr + A7*math.log(Ppr)**2 + A9/Tpr**2 + math.log(Ppr)*A11/Tpr
		B = 1 + A2*math.log(Ppr) + A4/Tpr + A6*math.log(Ppr)**2 + A8/Tpr**2 + math.log(Ppr)*A10/Tpr
		return round((math.log(A/B)),4)
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
	plt.title("Heidaryan, Moghdasi, & Rahimi's Correlation") 
	  
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

	for i in range(0,30):
		z = z_factor(Tpr, ppr)
		x.append(ppr)
		y.append(z)
		ppr = ppr + 0.1

	title = "Heidaryan's Correlation"
	xlabel = 'Pseudo-Reduced Pressure (Ppr)'
	ylabel = 'Compressibility Factor z'

	chart = get_plot(x, y, title, xlabel, ylabel)

	return chart


def table(Tpr = 1, Ppr = 1):

	#define figure and axes
	fig, ax = plt.subplots()

	#create values for table
	table_data=[]
	for i in range(1,10):

		z = z_factor(Tpr, Ppr)
		table_data.append([i, Tpr, Ppr, z])

		Ppr = Ppr + 0.1

	

	#create table
	table = ax.table(cellText=table_data, colLabels=['No.', 'Tpr', 'Ppr', 'Z Factor'], loc='center')

	#modify table
	ax.axis('off')

	#display table
	plt.show()