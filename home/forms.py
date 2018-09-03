from django import forms 
import re #regular exception
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

#AuthenticationForm loginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class RegisterForm(UserCreationForm):
	first_name = forms.CharField(label='Tên:', max_length=10, widget=forms.TextInput(attrs={
		'class':'form-control', 'placeholder':'Nhập tên'}))
	last_name = forms.CharField(label='Họ:', max_length=10, widget=forms.TextInput(attrs={
		'class':'form-control', 'placeholder':'Nhập họ'}))
	email = forms.EmailField(label='Email:', widget=forms.TextInput(attrs={
		'class':'form-control', 'placeholder':'Nhập email'}))
	username = forms.CharField(label='Tài khoản:', max_length=30, widget=forms.TextInput(attrs={
		'class':'form-control', 'placeholder':'Nhập tên tài khoản'}))
	password1 = forms.CharField(label='Mật khẩu:', widget=forms.PasswordInput(attrs={
		'class':'form-control', 'placeholder':'Nhập mật khẩu'}))
	password2 = forms.CharField(label='Nhập lại mật khẩu:', widget=forms.PasswordInput(attrs={
		'class':'form-control', 'placeholder':'Nhập lại mật khẩu'}))

	#check username
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username): #^$: all string, \w+: all lower, 
			raise forms.ValidationError("Username not accepting special characters.")
		
		MIN_LENGTH = 5
		#check len username
		if len(username) <= MIN_LENGTH:
			raise forms.ValidationError('The username must be at least %d characters.' % MIN_LENGTH)
			
		return username
		# #check usernam exist
		# try:
		# 	User.objects.get(username=username)
		# except ObjectDoesNotExist:
		# 	return username
		# raise forms.ValidationError("Username already exists.")

	# def clean_repassword(self):
	# 	#check password has
	# 	if 'password1' in self.cleaned_data:	
	# 		password1 = self.cleaned_data['password1']
	# 		password2 = self.cleaned_data['password2']

	# 		#check password = repassword and user input space continuous
	# 		if password1 == password2 and password1:
	# 			return password2
	# 	raise forms.ValidationError("The passwords do not match.")

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password1')

#login form
class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control', 'placeholder':'Tên đăng nhập'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control', 'placeholder':'Mật khẩu'}))

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']

		if username and password:
			self.user_cache = authenticate(username=username, password=password)
			if self.user_cache is None:
				raise forms.ValidationError("Please enter a correct username and password.")
		return self.cleaned_data