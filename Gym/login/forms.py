from django import forms
from django.forms import ModelForm
from .models import UserProfile,Offers,Machine,Dumbell,PlatesAndBar,OtherAccessory
from django.contrib.auth.models import User
class LoginForm(forms.Form):
	username = forms.CharField(max_length = 15)
	password = forms.CharField(max_length = 15,widget = forms.PasswordInput())
class UserProfileForm(ModelForm):
	class Meta:
		model= UserProfile
		fields=["age","gender","phoneno","address","status","bloodgrp","duration","needs_instructor"]

# class AddUserForm(ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm your password")
#     email = forms.CharField(required=True)

#     class Meta:
#         model = User
#         exclude = ['last_login', 'date_joined']

#     def clean(self):
#         super(SignUpForm, self).clean()
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password and password != confirm_password:
#             self._errors['password'] = self.error_class(['Passwords don\'t match'])
#         return self.cleaned_data

class AddUserForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput(),label="Confirm your Password")
	email = forms.CharField(required=True)
	first_name= forms.CharField(required=True, label="First Name")
	last_name= forms.CharField(required=True, label="Last Name")

	class Meta:
		model = User
		fields = ['username','password','confirm_password','first_name','last_name','email']
		#exclude = ['last_login','date_joined','is_superuser','is_staff','is_active','groups','user_permissions']

	def clean(self):
		super(AddUserForm, self).clean()
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			self._errors['password'] = self.error_class(['Passwords don\'t match'])
		return self.cleaned_data

class OffersForm(ModelForm):
	class Meta:
		model = Offers
		fields = ['offer']

class UserProfileForm1(ModelForm):
	exercises = forms.CharField(widget=forms.Textarea())
	class Meta:
		model = UserProfile
		fields = ['exercises']

class UserProfileForm2(ModelForm):
	diet = forms.CharField(widget=forms.Textarea())
	class Meta:
		model = UserProfile
		fields = ['diet']

class MachineForm(ModelForm):
	class Meta:
		model = Machine
		fields = ["name","qty"]

class DumbellForm(ModelForm):
	class Meta:
		model = Dumbell
		fields = ["name","qty"]

class PlatesAndBarForm(ModelForm):
	class Meta:
		model = PlatesAndBar
		fields = ["name","qty"]

class OtherAccessoryForm(ModelForm):
	class Meta:
		model = OtherAccessory
		fields = ["name","qty"]

class DietForm(forms.Form):
	fat = forms.IntegerField()
	protein = forms.IntegerField()
	carbohydrate = forms.IntegerField()