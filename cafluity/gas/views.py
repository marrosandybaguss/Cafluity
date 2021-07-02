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
			abiCorrelation = request.POST['abiCorrelation']
			bbCorrelation = request.POST['bbCorrelation']
			dakCorrelation = request.POST['da-kCorrelation']
			hyCorrelation = request.POST['hyCorrelation']
			hmrCorrelation = request.POST['hmrCorrelation']
			neCorrelation = request.POST['neCorrelation']
			snCorrelation = request.POST['snCorrelation']
			correlation = []
			if abiCorrelation != "false":
				correlation.append(abiCorrelation)
			if bbCorrelation != "false":
				correlation.append(bbCorrelation)
			if dakCorrelation != "false":
				correlation.append(dakCorrelation)
			if hyCorrelation != "false":
				correlation.append(hyCorrelation)
			if hmrCorrelation != "false":
				correlation.append(hmrCorrelation)
			if neCorrelation != "false":
				correlation.append(neCorrelation)
			if snCorrelation != "false":
				correlation.append(snCorrelation)
		
			pressureDensity = 2000
			temperatureDensity = 300
			molarDensity = 20.272
			zfactorDensity = 0.9612

			pressureSV = 2000
			temperatureSV = 300
			molarSV = 20.272
			zfactorSV = 0.9612

		elif realGasProperty == "density":
			pressureDensity = float(request.POST['pressureDensity'])
			temperatureDensity = float(request.POST['temperatureDensity'])
			molarDensity = float(request.POST['molarDensity'])
			zfactorDensity = float(request.POST['zfactorDensity'])
		
			Yg = 0.7
			pressure = 2000
			temperature = 300
			n2 = 3.0
			co2 = 6.0
			h2s = 4.0
			correlation = ["da-k", "hy"]

			pressureSV = 2000
			temperatureSV = 300
			molarSV = 20.272
			zfactorSV = 0.9612

		elif realGasProperty == "specificvolume":
			pressureSV = float(request.POST['pressureSV'])
			temperatureSV = float(request.POST['temperatureSV'])
			molarSV = float(request.POST['molarSV'])
			zfactorSV = float(request.POST['zfactorSV'])
		
			Yg = 0.7
			pressure = 2000
			temperature = 300
			n2 = 3.0
			co2 = 6.0
			h2s = 4.0
			correlation = ["da-k", "hy"]

			pressureDensity = 2000
			temperatureDensity = 300
			molarDensity = 20.272
			zfactorDensity = 0.9612
	
	else:
		realGasProperty = "zfactor"

		Yg = 0.7
		pressure = 2000
		temperature = 300
		n2 = 3.0
		co2 = 6.0
		h2s = 4.0
		correlation = ["da-k", "hy"]

		pressureDensity = 2000
		temperatureDensity = 300
		molarDensity = 20.272
		zfactorDensity = 0.9612

		pressureSV = 2000
		temperatureSV = 300
		molarSV = 20.272
		zfactorSV = 0.9612

	return realGasProperty, Yg, pressure, temperature, n2, co2, h2s, correlation, pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressureSV, temperatureSV, molarSV, zfactorSV

def realgas_zfactor(correlation, Yg, pressure, temperature, n2, co2, h2s):
	Tpc, ppc = zfac.pseudo_critical(Yg, co2, h2s, n2)

	temperatureConv = conv.temp_FR(temperature)
	Tpr, ppr = zfac.pseudo_reduced(temperatureConv, pressure, Tpc, ppc)
	zfactors = []
	zfactorGraphs = []
	boundaryBool = 	1
	boundaries = []

	for corr in correlation:
		name, boundary, zfactor = rgas.z(Tpr, ppr, corr)
		if zfactor != "NULL":
			zfactors.append({"corr": corr, "name": name, "zfactor": zfactor})
			zfactorGraphs.append(rgas.z_graph(Tpr, ppr, corr))
		else :
			boundaryBool = 0
			if boundary["noPpr"] != "NULL":
				boundaries.append({"name": name, "PprBoundary": boundary["PprBoundary"], "TprBoundary": boundary["TprBoundary"], "noPprBoundary": boundary["noPpr"]})
			else :
				boundaries.append({"name": name, "PprBoundary": boundary["PprBoundary"], "TprBoundary": boundary["TprBoundary"]})
			

	return Tpc, ppc, temperatureConv, Tpr, ppr, boundaryBool, zfactors, boundaries, zfactorGraphs

def realgas_density(pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressure, temperatureConv, Yg, zfactors):
	temperatureConvDensity = conv.temp_FR(temperatureDensity)
	density = rgas.rho_g(pressureDensity, temperatureConvDensity, molarDensity, zfactorDensity)
	correlationDensities = []

	for z in zfactors:
		correlationDensities.append({"name": z["name"], "density": rgas.rho_g(pressure, temperatureConv, rgas.Ma(Yg), z["zfactor"])})

	return density, correlationDensities

def realgas_specificvolume(pressureSV, temperatureSV, molarSV, zfactorSV, pressure, temperatureConv, Yg, zfactors):
	temperatureConvSV = conv.temp_FR(temperatureSV)
	specificvolume = rgas.v(pressureSV, temperatureConvSV, molarSV, zfactorSV)
	correlationSpecificvolumes = []

	for z in zfactors:
		correlationSpecificvolumes.append({"name": z["name"], "specificvolume": rgas.v(pressure, temperatureConv, rgas.Ma(Yg), z["zfactor"])})

	return specificvolume, correlationSpecificvolumes

def real_gas(request):
	realGasProperty, Yg, pressure, temperature, n2, co2, h2s, correlation, pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressureSV, temperatureSV, molarSV, zfactorSV = realgas_var(request)

	Tpc, ppc, temperatureConv, Tpr, ppr, boundaryBool, zfactors, boundaries, zfactorGraphs = realgas_zfactor(correlation, Yg, pressure, temperature, n2, co2, h2s)

	density, correlationDensities = realgas_density(pressureDensity, temperatureDensity, molarDensity, zfactorDensity, pressure, temperatureConv, Yg, zfactors)

	specificvolume, correlationSpecificvolumes = realgas_specificvolume(pressureSV, temperatureSV, molarSV, zfactorSV, pressure, temperatureConv, Yg, zfactors)
	
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
		'correlation': correlation,
		'boundaryBool': boundaryBool,
		'zfactors': zfactors,
		'zfactorGraphs': zfactorGraphs,
		'boundaries': boundaries,
		# Density
		'pressureDensity': pressureDensity,
		'temperatureDensity': temperatureDensity,
		'molarDensity': molarDensity,
		'zfactorDensity': zfactorDensity,
		'density': density,
		'correlationDensities': correlationDensities,
		# Specific Volume
		'pressureSV': pressureSV,
		'temperatureSV': temperatureSV,
		'molarSV': molarSV,
		'zfactorSV': zfactorSV,
		'specificvolume': specificvolume,
		'correlationSpecificvolumes': correlationSpecificvolumes,
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

def reference(request):
	if request.method == "GET" and 'ref' in request.GET:
		activeURL = request.GET['ref']
	else:
		activeURL = 'p'
	
	context = {
		'activeURL': activeURL
	}
	return render(request, 'gas/reference.html', context)