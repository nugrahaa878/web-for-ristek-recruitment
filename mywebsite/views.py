from django.shortcuts import render


def index(request):
	context = {
		'judul' : 'PengenBelajardiRistek',
		'subjudul' : 'Homepage',
	}

	return render(request, 'index.html', context)