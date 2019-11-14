from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectDateWidget
import datetime
from .models import Forum, Comment
 
class PostForm(forms.Form):
	title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Post Title'}))
	desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '   Post Description','rows':8, 'cols':15}))
	mini_desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '   A Small Description','rows':4, 'cols':15}))
	image = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Image URL'}))
	image_credits = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Image Credits'}))
	class Meta:
		model = Forum
		fields = ('title','desc','mini_desc','image','image_credits')

class CommentForm(forms.ModelForm):
	name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Post Title','class':"form-control"}))
	desc = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'placeholder': '   Post Description','rows':8, 'cols':15}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control",'placeholder': 'Email'}))
	
	class Meta:
		model = Comment
		fields = ('name', 'email', 'desc')