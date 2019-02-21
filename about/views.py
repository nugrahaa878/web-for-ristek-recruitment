from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'judul'	: 'AboutThisMan',
		'subjudul' : 'This is me'
	}


	return render(request, 'about/index.html', context)