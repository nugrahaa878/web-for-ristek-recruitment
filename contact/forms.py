from django import forms

class FormField(forms.Form):
	Nama = forms.CharField(max_length=50)
	Komentar = forms.CharField(
		max_length=500,
		widget = forms.Textarea,
	)
