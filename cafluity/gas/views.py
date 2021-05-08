from django.shortcuts import render

from .main import base_zfactor as zfac
from .main import convertion as conv
from .main import real_gas as rgas
from .main import ideal_gas as igas

def get_realgas_var(request):
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
			molarDensity = 20.272
			zfactorDensity = 0.9612

			pressureSV = 1000
			temperatureSV = 300
			molarSV = 20.272
			zfactorSV = 0.9612

		elif realGasProperty == "density":
			pressureDensity = float(request.POST['pressureDensity'])
			temperatureDensity = float(request.POST['temperatureDensity'])
			molarDensity = float(request.POST['molarDensity'])
			zfactorDensity = float(request.POST['zfactorDensity'])
		
			Yg = 0.7
			pressure = 1000
			temperature = 300
			n2 = 3.0
			co2 = 6.0
			h2s = 4.0

			pressureSV = 1000
			temperatureSV = 300
			molarSV = 20.272
			zfactorSV = 0.9612

		elif realGasProperty == "specificvolume":
			pressureSV = float(request.POST['pressureSV'])
			temperatureSV = float(request.POST['temperatureSV'])
			molarSV = float(request.POST['molarSV'])
			zfactorSV = float(request.POST['zfactorSV'])
		
			Yg = 0.7
			pressure = 1000
			temperature = 300
			n2 = 3.0
			co2 = 6.0
			h2s = 4.0

			pressureDensity = 1000
			temperatureDensity = 300
			molarDensity = 20.272
			zfactorDensity = 0.9612
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
		molarDensity = 20.272
		zfactorDensity = 0.9612

		pressureSV = 1000
		temperatureSV = 300
		molarSV = 20.272
		zfactorSV = 0.9612

	return realGasProperty, Yg, pressure, temperature, n2, co2, h2s, pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressureSV, temperatureSV, molarSV, zfactorSV

def zfactor(Yg, pressure, temperature, n2, co2, h2s):
	Tpc, ppc = zfac.pseudo_critical(Yg, co2, h2s, n2)

	T_conv = conv.temp_FR(temperature)
	Tpr, ppr = zfac.pseudo_reduced(T_conv, pressure, Tpc, ppc)

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

	return Tpc, ppc, T_conv, Tpr, ppr, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari, drancukChart, hallYarboroughChart, brillBeggChart, newExplicitChart, aziziChart, heidaryanChart, sanjariChart

def density(pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressure, T_conv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari):
	temperatureDensity = conv.temp_FR(temperatureDensity)
	density = rgas.rho_g(pressureDensity, temperatureDensity, molarDensity, zfactorDensity)

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

	return density, densityDrancuk, densityHallYarborough, densityBrillBegg, densityNewExplicit, densityAzizi, densityHeidaryan, densitySanjari

def specific_volume(pressureSV, temperatureSV, molarSV, zfactorSV, pressure, T_conv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari):
	temperatureSV = conv.temp_FR(temperatureSV)
	specificvolume = rgas.v(pressureSV, temperatureSV, molarSV, zfactorSV)

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

	return specificvolume, svDrancuk, svHallYarborough, svBrillBegg, svNewExplicit, svAzizi, svHeidaryan, svSanjari

def real_gas(request):
	realGasProperty, Yg, pressure, temperature, n2, co2, h2s, pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressureSV, temperatureSV, molarSV, zfactorSV = get_realgas_var(request)

	Tpc, ppc, T_conv, Tpr, ppr, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari, drancukChart, hallYarboroughChart, brillBeggChart, newExplicitChart, aziziChart, heidaryanChart, sanjariChart = zfactor(Yg, pressure, temperature, n2, co2, h2s)

	densityvar, densityDrancuk, densityHallYarborough, densityBrillBegg, densityNewExplicit, densityAzizi, densityHeidaryan, densitySanjari = density(pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressure, T_conv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari)

	specificvolume, svDrancuk, svHallYarborough, svBrillBegg, svNewExplicit, svAzizi, svHeidaryan, svSanjari = specific_volume(pressureSV, temperatureSV, molarSV, zfactorSV, pressure, T_conv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari)
	
	context = {
		'realGasProperty': realGasProperty,
		# zfactor
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
		'molarDensity': molarDensity,
		'zfactorDensity': zfactorDensity,
		'density': densityvar,
		'densityDrancuk': densityDrancuk,
		'densityHallYarborough': densityHallYarborough,
		'densityBrillBegg': densityBrillBegg,
		'densityNewExplicit': densityNewExplicit,
		'densityAzizi': densityAzizi,
		'densityHeidaryan': densityHeidaryan,
		'densitySanjari': densitySanjari,
		# Specific Volume
		'pressureSV': pressureSV,
		'temperatureSV': temperatureSV,
		'molarSV': molarSV,
		'zfactorSV': zfactorSV,
		'specificvolume': specificvolume,
		'svDrancuk': svDrancuk,
		'svHallYarborough': svHallYarborough,
		'svBrillBegg': svBrillBegg,
		'svNewExplicit': svNewExplicit,
		'svAzizi': svAzizi,
		'svHeidaryan': svHeidaryan,
		'svSanjari': svSanjari,
	}

	return render(request, 'gas/real-gas.html', context)

def ideal_gas(request):
	if request.method == "POST":
		idealGasProperty = request.POST['idealGasProperty']
		if idealGasProperty == "molecularweight":
			gasGravityMW = float(request.POST['gasGravityMW'])
			molecularAirMW = float(request.POST['molecularAirMW'])
		
			# pressureDensity = 1000
			# temperatureDensity = 300
			# molarDensity = 20.272
			# zfactorDensity = 0.9612
	else:
		idealGasProperty = "molecularweight"

		gasGravityMW = 0.7
		molecularAirMW = 28.96

	molecularWeight = igas.Ma(gasGravityMW, molecularAirMW)
	
	context = {
		'idealGasProperty': idealGasProperty,
		'gasGravityMW': gasGravityMW,
		'molecularAirMW': molecularAirMW,
		'molecularWeight': molecularWeight,
	}
	return render(request, 'gas/ideal-gas.html', context)