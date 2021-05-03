from django.shortcuts import render
from .main import base_zfactor as zfac

# Create your views here.

def index(request):
	if request.method == "POST":
		gasGravity = float(request.POST['gas-gravity'])
		pressure = float(request.POST['pressure'])
		temperature = float(request.POST['temperature'])
		nitrogen = float(request.POST['nitrogen'])
		carbonDioxide = float(request.POST['carbon-dioxide'])
		hydrogenSulfide = float(request.POST['hydrogen-sulfide'])
	else:
		gasGravity = 0.7
		pressure = 1000
		temperature = 300
		nitrogen = 3.0
		carbonDioxide = 6.0
		hydrogenSulfide = 4.0

	Tpc, ppc = zfac.pseudo_critical(gasGravity, carbonDioxide, hydrogenSulfide, nitrogen)

	context = {
		'title':'Compressibility Factor Z',
		'gasGravity': gasGravity,
		'pressure': pressure,
		'temperature': temperature,
		'nitrogen': nitrogen,
		'carbonDioxide': carbonDioxide,
		'hydrogenSulfide': hydrogenSulfide,
		'Tpc': Tpc,
		'ppc': ppc,
	}
	return render(request, 'gas/index.html', context)
