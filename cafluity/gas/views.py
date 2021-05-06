from django.shortcuts import render
import matplotlib.pyplot as plt

from .main import base_zfactor as zfac
from .main import convertion as conv
from .main import real_gas as rgas
# from .utils import get_plot

# Create your views here.

def index(request):
	if request.method == "POST":
		Yg = float(request.POST['gas-gravity'])
		pressure = float(request.POST['pressure'])
		temperature = float(request.POST['temperature'])
		n2 = float(request.POST['nitrogen'])
		co2 = float(request.POST['carbon-dioxide'])
		h2s = float(request.POST['hydrogen-sulfide'])
	else:
		Yg = 0.7
		pressure = 1000
		temperature = 300
		n2 = 3.0
		co2 = 6.0
		h2s = 4.0

	# Calculate Pseudo Critical
	Tpc, ppc = zfac.pseudo_critical(Yg, co2, h2s, n2)
	# Calculate Pseudo Reduced
	T_conv = conv.temp_FR(temperature)
	Tpr, ppr = zfac.pseudo_reduced(T_conv, pressure, Tpc, ppc)
	# Compressibility Factor Z
	zDrancuk = rgas.z(Tpr, ppr, "da-k")
	zHallYarborough = rgas.z(Tpr, ppr, "hy")
	zBrillBegg = rgas.z(Tpr, ppr, "bb")
	zNewExplicit = rgas.z(Tpr, ppr, "ne")
	zAzizi = rgas.z(Tpr, ppr, "abi")
	zHeidaryan = rgas.z(Tpr, ppr, "hmr")
	zSanjari = rgas.z(Tpr, ppr, "sn")

	chart = rgas.z_graph(Tpr, ppr, "ne")
	# chart = get_plot(x, y)

	context = {
		'title':'Compressibility Factor Z',
		'gasGravity': Yg,
		'pressure': pressure,
		'temperature': temperature,
		'nitrogen': n2,
		'carbonDioxide': co2,
		'hydrogenSulfide': h2s,
		'Tpc': Tpc,
		'ppc': ppc,
		'Tpr': Tpr,
		'ppr': ppr,
		'zDrancuk': zDrancuk,
		'zHallYarborough': zHallYarborough,
		'zBrillBegg': zBrillBegg,
		'zNewExplicit': zNewExplicit,
		'zAzizi': zAzizi,
		'zHeidaryan': zHeidaryan,
		'zSanjari': zSanjari,
		'chart': chart,
	}

	plt.show()

	return render(request, 'gas/index.html', context)
