from django.shortcuts import render

from .main import base_zfactor as zfac
from .main import convertion as conv
from .main import real_gas as rgas
from .main import ideal_gas as igas

def realgas_var(request):
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

	temperatureConv = conv.temp_FR(temperature)
	Tpr, ppr = zfac.pseudo_reduced(temperatureConv, pressure, Tpc, ppc)

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

	return Tpc, ppc, temperatureConv, Tpr, ppr, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari, drancukChart, hallYarboroughChart, brillBeggChart, newExplicitChart, aziziChart, heidaryanChart, sanjariChart

def realgas_density(pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressure, temperatureConv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari):
	temperatureConvDensity = conv.temp_FR(temperatureDensity)
	density = rgas.rho_g(pressureDensity, temperatureConvDensity, molarDensity, zfactorDensity)

	if zDrancuk != "NULL":
		densityDrancuk = rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), zDrancuk)
	else:
		densityDrancuk = "NULL"
	if zHallYarborough != "NULL":
		densityHallYarborough = rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), zHallYarborough)
	else:
		densityHallYarborough = "NULL"
	if zBrillBegg != "NULL":
		densityBrillBegg = rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), zBrillBegg)
	else:
		densityBrillBegg = "NULL"
	if zNewExplicit != "NULL":
		densityNewExplicit = rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), zNewExplicit)
	else:
		densityNewExplicit = "NULL"
	if zAzizi != "NULL":
		densityAzizi = rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), zAzizi)
	else:
		densityAzizi = "NULL"
	if zHeidaryan != "NULL":
		densityHeidaryan = rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), zHeidaryan)
	else:
		densityHeidaryan = "NULL"
	if zSanjari != "NULL":
		densitySanjari = rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), zSanjari)
	else:
		densitySanjari = "NULL"

	return density, densityDrancuk, densityHallYarborough, densityBrillBegg, densityNewExplicit, densityAzizi, densityHeidaryan, densitySanjari

def realgas_specificvolume(pressureSV, temperatureSV, molarSV, zfactorSV, pressure, temperatureConv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari):
	temperatureConvSV = conv.temp_FR(temperatureSV)
	specificvolume = rgas.v(pressureSV, temperatureConvSV, molarSV, zfactorSV)

	if zDrancuk != "NULL":
		svDrancuk = rgas.v(pressure, temperatureConv, rgas.Ma(Yg), zDrancuk)
	else:
		svDrancuk = "NULL"
	if zHallYarborough != "NULL":
		svHallYarborough = rgas.v(pressure, temperatureConv, rgas.Ma(Yg), zHallYarborough)
	else:
		svHallYarborough = "NULL"
	if zBrillBegg != "NULL":
		svBrillBegg = rgas.v(pressure, temperatureConv, rgas.Ma(Yg), zBrillBegg)
	else:
		svBrillBegg = "NULL"
	if zNewExplicit != "NULL":
		svNewExplicit = rgas.v(pressure, temperatureConv, rgas.Ma(Yg), zNewExplicit)
	else:
		svNewExplicit = "NULL"
	if zAzizi != "NULL":
		svAzizi = rgas.v(pressure, temperatureConv, rgas.Ma(Yg), zAzizi)
	else:
		svAzizi = "NULL"
	if zHeidaryan != "NULL":
		svHeidaryan = rgas.v(pressure, temperatureConv, rgas.Ma(Yg), zHeidaryan)
	else:
		svHeidaryan = "NULL"
	if zSanjari != "NULL":
		svSanjari = rgas.v(pressure, temperatureConv, rgas.Ma(Yg), zSanjari)
	else:
		svSanjari = "NULL"

	return specificvolume, svDrancuk, svHallYarborough, svBrillBegg, svNewExplicit, svAzizi, svHeidaryan, svSanjari

def real_gas(request):
	realGasProperty, Yg, pressure, temperature, n2, co2, h2s, pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressureSV, temperatureSV, molarSV, zfactorSV = realgas_var(request)

	Tpc, ppc, temperatureConv, Tpr, ppr, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari, drancukChart, hallYarboroughChart, brillBeggChart, newExplicitChart, aziziChart, heidaryanChart, sanjariChart = zfactor(Yg, pressure, temperature, n2, co2, h2s)

	density, densityDrancuk, densityHallYarborough, densityBrillBegg, densityNewExplicit, densityAzizi, densityHeidaryan, densitySanjari = realgas_density(pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressure, temperatureConv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari)

	specificvolume, svDrancuk, svHallYarborough, svBrillBegg, svNewExplicit, svAzizi, svHeidaryan, svSanjari = realgas_specificvolume(pressureSV, temperatureSV, molarSV, zfactorSV, pressure, temperatureConv, Yg, zDrancuk, zHallYarborough, zBrillBegg, zNewExplicit, zAzizi, zHeidaryan, zSanjari)
	
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
		'density': density,
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

def idealgas_var(request):
	if request.method == "POST":
		idealGasProperty = request.POST['idealGasProperty']
		if idealGasProperty == "molecularweight":
			gasGravityMW = float(request.POST['gasGravityMW'])
			molecularAirMW = float(request.POST['molecularAirMW'])
		
			molarDensity = igas.Ma(gasGravityMW, molecularAirMW)
			pressureDensity = 50.0
			temperatureDensity = 20.0

			molarSV = igas.Ma(gasGravityMW, molecularAirMW)
			pressureSV = 50.0
			temperatureSV = 20.0

			molarGravity = igas.Ma(gasGravityMW, molecularAirMW)
			molecularAirSG = 28.96

		elif idealGasProperty == "density":
			molarDensity = float(request.POST['molarDensity'])
			pressureDensity = float(request.POST['pressureDensity'])
			temperatureDensity = float(request.POST['temperatureDensity'])
		
			gasGravityMW = 0.7
			molecularAirMW = 28.96

			molarSV = 20.272
			pressureSV = 50.0
			temperatureSV = 20.0

			molarGravity = 20.272
			molecularAirSG = 28.96

		elif idealGasProperty == "specificvolume":
			molarSV = float(request.POST['molarSV'])
			pressureSV = float(request.POST['pressureSV'])
			temperatureSV = float(request.POST['temperatureSV'])

			gasGravityMW = 0.7
			molecularAirMW = 28.96

			molarDensity = 20.272
			pressureDensity = 50.0
			temperatureDensity = 20.0

			molarGravity = 20.272
			molecularAirSG = 28.96

		elif idealGasProperty == "specificgravity":
			molarGravity = float(request.POST['molarGravity'])
			molecularAirSG = float(request.POST['molecularAirSG'])

			gasGravityMW = 0.7
			molecularAirMW = 28.96

			molarDensity = 20.272
			pressureDensity = 50.0
			temperatureDensity = 20.0

			molarSV = 20.272
			pressureSV = 50.0
			temperatureSV = 20.0

	else:
		idealGasProperty = "molecularweight"

		gasGravityMW = 0.7
		molecularAirMW = 28.96

		molarDensity = 20.272
		pressureDensity = 50.0
		temperatureDensity = 20.0

		molarSV = 20.272
		pressureSV = 50.0
		temperatureSV = 20.0

		molarGravity = 20.272
		molecularAirSG = 28.96

	return idealGasProperty, gasGravityMW, molecularAirMW, molarDensity, pressureDensity, temperatureDensity, molarSV, pressureSV, temperatureSV, molarGravity, molecularAirSG

def ideal_gas(request):
	idealGasProperty, gasGravityMW, molecularAirMW, molarDensity, pressureDensity, temperatureDensity, molarSV, pressureSV, temperatureSV, molarGravity, molecularAirSG = idealgas_var(request)

	molecularWeight = igas.Ma(gasGravityMW, molecularAirMW)

	temperatureConvDensity = conv.temp_FR(temperatureDensity)
	density = igas.rho_g(pressureDensity, molarDensity, temperatureConvDensity)

	temperatureConvSV = conv.temp_FR(temperatureSV)
	specificvolume = igas.v(pressureSV, molarSV, temperatureConvSV)

	specificgravity = igas.Yg(molarGravity, molecularAirSG)
	
	context = {
		'idealGasProperty': idealGasProperty,
		# Molecular Weight
		'gasGravityMW': gasGravityMW,
		'molecularAirMW': molecularAirMW,
		'molecularWeight': molecularWeight,
		# Density
		'molarDensity': molarDensity,
		'pressureDensity': pressureDensity,
		'temperatureDensity': temperatureDensity,
		'density': density,
		# Specific Volume
		'molarSV': molarSV,
		'pressureSV': pressureSV,
		'temperatureSV': temperatureSV,
		'specificvolume': specificvolume,
		# Specific Gravity
		'molarGravity': molarGravity,
		'molecularAirSG': molecularAirSG,
		'specificgravity': specificgravity,
	}
	
	return render(request, 'gas/ideal-gas.html', context)
