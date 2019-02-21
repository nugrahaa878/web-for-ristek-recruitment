from django.shortcuts import render

# Create your views here.

from .forms import FormField
from .models import PostModel

def index(request):
	posts = PostModel.objects.all()

	form_field = FormField()

	context = {
		'judul' : 'MyContact',
		'subjudul' : "Call me, im single",
		'data_form' : form_field,
		'posts' : posts,
	}

	if request.method == "POST":
		PostModel.objects.create(
			nama = request.POST['Nama'],
			komentar = request.POST['Komentar'],
		)

	return render(request, 'contact/index.html', context)