from django.shortcuts import render

# Create your views here.

def index(request):
	if request.method == "POST":
		gasGravity = request.POST['gas-gravity']
		pressure = request.POST['pressure']
		temperature = request.POST['temperature']
		nitrogen = request.POST['nitrogen']
		carbonDioxide = request.POST['carbon-dioxide']
		hydrogenSulfide = request.POST['hydrogen-sulfide']
	else:
		gasGravity = 0.7
		pressure = 1000
		temperature = 300
		nitrogen = 3.0
		carbonDioxide = 6.0
		hydrogenSulfide = 4.0

	context = {
		'title':'Compressibility Factor Z',
		'gasGravity': gasGravity,
		'pressure': pressure,
		'temperature': temperature,
		'nitrogen': nitrogen,
		'carbonDioxide': carbonDioxide,
		'hydrogenSulfide': hydrogenSulfide,
	}
	return render(request, 'gas/index.html', context)
