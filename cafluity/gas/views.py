from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'Compressibility Factor Z',
		# 'kontributor':'Faqizah',
		# 'nav':[
		# 	['/','Home'],
		# 	['/blog','Blog'],
		# 	['/about','About'],
		# 	['/blog/olahraga','Blog Olahraga'],
		# ],
	}
	return render(request, 'gas/index.html', context)
