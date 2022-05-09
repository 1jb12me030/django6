# import email
# from django import forms
# class StudentRegistration(forms.Form):
#     name=forms.CharField(max_length=64)
#     email=forms.EmailField()

from django import forms

# creating a form
class StudentRegistration(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)
	password = forms.CharField(widget = forms.PasswordInput())

