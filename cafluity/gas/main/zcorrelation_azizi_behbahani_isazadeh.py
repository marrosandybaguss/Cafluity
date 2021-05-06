"""
temperature range of 1.1 <= Tpr <= 2
pressure range of 0.2 <= Ppr <= 11
"""
import math
import matplotlib.pyplot as plt
from .graph import get_plot

maxTpr = 2
minTpr = 1.1
maxPpr = 11
minPpr = 0.2

a = 0.0373142485385592
b = -0.0140807151485369
c = 0.0163263245387186
d = -0.0307776478819813
e = 13843575480.943800
f = -16799138540.763700
g = 1624178942.6497600
h = 13702270281.086900
i = -41645509.896474600
j = 237249967625.01300
k = -24449114791.1531
l = 19357955749.3274
m = -126354717916.607
n = 623705678.385784
o = 17997651104.3330
p = 151211393445.064
q = 139474437997.172
r = -24233012984.0950
s = 18938047327.5205
t = -141401620722.689

def boundary_check(Tpr, Ppr):
	if Tpr < minTpr or Tpr > maxTpr:
		return 0
	
	if Ppr < minPpr or Ppr > maxPpr:
		return 0

	return 1

def z_factor(Tpr = 1, Ppr = 1):
	if boundary_check(Tpr, Ppr):

		A = a*Tpr**2.16 + b*Ppr**1.028 + c*(Ppr**1.58)*(Tpr**(-2.1)) + d*math.log(Tpr**(-0.5))
		B = e + f*Tpr**2.4 + g*Ppr**1.56 + h*(Ppr**0.124)*(Tpr**3.033)
		C = i*math.log(Tpr)**(-1.28) + j*math.log(Tpr)**1.37 + k*math.log(Ppr) + l*math.log(Ppr)**2 + m*math.log(Ppr)*math.log(Tpr)
		D = 1 + n*Tpr**5.55 + o*(Ppr**0.68)*(Tpr**0.33)
		E = p*math.log(Tpr)**1.18 + q*math.log(Tpr)**2.1 + r*math.log(Ppr) + s*math.log(Ppr)**2 + t*math.log(Ppr)*math.log(Tpr)
		return round((A + (B + C)/(D + E)),4)

	else:
		return "NULL"

def muliti_graph(Tpr = 1, Ppr = 1):
	
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
	plt.title("Azizi, Behbahani, & Isazadeh's Correlation") 
	  
	# function to show the plot 
	plt.show()


def graph(Tpr = 1, Ppr = 1):
	ppr = Ppr - 1.5
	x = []
	y = []

	for i in range(1,30):
		ppr = ppr + 0.1
		z = z_factor(Tpr, ppr)
		x.append(ppr)
		y.append(z)

	title = "Azizi Behbahani Isazadeh's Correlation"
	xlabel = 'Pseudoreduced Pressure Ppr'
	ylabel = 'Compressibility Factor z'

	chart = get_plot(x, y, title, xlabel, ylabel)

	return chart
