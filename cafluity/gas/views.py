from django.shortcuts import render

from .main import base_zfactor as zfac
from .main import convertion as conv
from .main import real_gas as rgas


def real_gas(request):
	if request.method == "POST":
		realGasProperty = request.POST['realGasProperty']
		if realGasProperty == "zfactor":
			Yg = float(request.POST['gas-gravity'])
			pressure = float(request.POST['pressure'])
			temperature = float(request.POST['temperature'])
			n2 = float(request.POST['nitrogen'])
			co2 = float(request.POST['carbon-dioxide'])
			h2s = float(request.POST['hydrogen-sulfide'])
		
			pressureDensity = 1000
			temperatureDensity = 300
			Ma = rgas.Ma(Yg)
			zfactorDensity = 0.9612

		elif realGasProperty == "density":
			pressureDensity = float(request.POST['pressureDensity'])
			temperatureDensity = float(request.POST['temperatureDensity'])
			Ma = float(request.POST['molarDensity'])
			zfactorDensity = float(request.POST['zfactorDensity'])
		
			Yg = 0.7
			pressure = 1000
			temperature = 300
			n2 = 3.0
			co2 = 6.0
			h2s = 4.0
	else:
		realGasProperty = "zfactor"

		Yg = 0.7
		pressure = 1000
		temperature = 300
		n2 = 3.0
		co2 = 6.0
		h2s = 4.0

		pressureDensity = 1000
		temperatureDensity = 300
		Ma = rgas.Ma(Yg)
		zfactorDensity = 0.9612

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

	drancukChart = rgas.z_graph(Tpr, ppr, "da-k")
	hallYarboroughChart = rgas.z_graph(Tpr, ppr, "hy")
	brillBeggChart = rgas.z_graph(Tpr, ppr, "bb")
	newExplicitChart = rgas.z_graph(Tpr, ppr, "ne")
	aziziChart = rgas.z_graph(Tpr, ppr, "abi")
	heidaryanChart = rgas.z_graph(Tpr, ppr, "hmr")
	sanjariChart = rgas.z_graph(Tpr, ppr, "sn")

	# Density
	density = rgas.rho_g(pressureDensity, temperatureDensity, Ma, zfactorDensity)
	if zDrancuk != "NULL":
		densityDrancuk = rgas.rho_g(pressure, T_conv, rgas.Ma(Yg), zDrancuk)
	else:
		densityDrancuk = "NULL"
	if zHallYarborough != "NULL":
		densityHallYarborough = rgas.rho_g(pressure, T_conv, rgas.Ma(Yg), zHallYarborough)
	else:
		densityHallYarborough = "NULL"
	if zBrillBegg != "NULL":
		densityBrillBegg = rgas.rho_g(pressure, T_conv, rgas.Ma(Yg), zBrillBegg)
	else:
		densityBrillBegg = "NULL"
	if zNewExplicit != "NULL":
		densityNewExplicit = rgas.rho_g(pressure, T_conv, rgas.Ma(Yg), zNewExplicit)
	else:
		densityNewExplicit = "NULL"
	if zAzizi != "NULL":
		densityAzizi = rgas.rho_g(pressure, T_conv, rgas.Ma(Yg), zAzizi)
	else:
		densityAzizi = "NULL"
	if zHeidaryan != "NULL":
		densityHeidaryan = rgas.rho_g(pressure, T_conv, rgas.Ma(Yg), zHeidaryan)
	else:
		densityHeidaryan = "NULL"
	if zSanjari != "NULL":
		densitySanjari = rgas.rho_g(pressure, T_conv, rgas.Ma(Yg), zSanjari)
	else:
		densitySanjari = "NULL"


	# Specific Volume
	# specificvolume = rgas.rho_g(pressureSV, temperatureSV, Ma, zfactorSV)
	if zDrancuk != "NULL":
		svDrancuk = rgas.v(pressure, T_conv, rgas.Ma(Yg), zDrancuk)
	else:
		svDrancuk = "NULL"
	if zHallYarborough != "NULL":
		svHallYarborough = rgas.v(pressure, T_conv, rgas.Ma(Yg), zHallYarborough)
	else:
		svHallYarborough = "NULL"
	if zBrillBegg != "NULL":
		svBrillBegg = rgas.v(pressure, T_conv, rgas.Ma(Yg), zBrillBegg)
	else:
		svBrillBegg = "NULL"
	if zNewExplicit != "NULL":
		svNewExplicit = rgas.v(pressure, T_conv, rgas.Ma(Yg), zNewExplicit)
	else:
		svNewExplicit = "NULL"
	if zAzizi != "NULL":
		svAzizi = rgas.v(pressure, T_conv, rgas.Ma(Yg), zAzizi)
	else:
		svAzizi = "NULL"
	if zHeidaryan != "NULL":
		svHeidaryan = rgas.v(pressure, T_conv, rgas.Ma(Yg), zHeidaryan)
	else:
		svHeidaryan = "NULL"
	if zSanjari != "NULL":
		svSanjari = rgas.v(pressure, T_conv, rgas.Ma(Yg), zSanjari)
	else:
		svSanjari = "NULL"


	context = {
		'title':'Compressibility Factor Z',
		'realGasProperty': realGasProperty,
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
		'drancukChart': drancukChart,
		'hallYarboroughChart': hallYarboroughChart,
		'brillBeggChart': brillBeggChart,
		'newExplicitChart': newExplicitChart,
		'aziziChart': aziziChart,
		'heidaryanChart': heidaryanChart,
		'sanjariChart': sanjariChart,
		# Density
		'pressureDensity': pressureDensity,
		'temperatureDensity': temperatureDensity,
		'molarDensity': Ma,
		'zfactorDensity': zfactorDensity,
		'density': density,
		'densityDrancuk': densityDrancuk,
		'densityHallYarborough': densityHallYarborough,
		'densityBrillBegg': densityBrillBegg,
		'densityNewExplicit': densityNewExplicit,
		'densityAzizi': densityAzizi,
		'densityHeidaryan': densityHeidaryan,
		'densitySanjari': densitySanjari,
		# Specific Volume
		# 'pressureDensity': pressureDensity,
		# 'temperatureDensity': temperatureDensity,
		# 'molarDensity': Ma,
		# 'zfactorDensity': zfactorDensity,
		# 'density': density,
		'svDrancuk': svDrancuk,
		'svHallYarborough': svHallYarborough,
		'svBrillBegg': svBrillBegg,
		'svNewExplicit': svNewExplicit,
		'svAzizi': svAzizi,
		'svHeidaryan': svHeidaryan,
		'svSanjari': svSanjari,
	}

	return render(request, 'gas/index.html', context)
