from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Forum,Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
	posts = Forum.objects.all()
	return render(request,'index.html',{'data':posts})

def forum(request,forum_id):
	if request.method == 'POST':
		print(request)
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			post = Forum.objects.get(id = forum_id)
			new_comment = comment_form.save(commit=False)
			new_comment.forum = post
			new_comment.save()
			posts = Forum.objects.get(id=forum_id)
			comments = Comment.objects.filter(forum = posts)
			comment_form = CommentForm()
			return render(request,'forum.html',{'title':posts.title,'id':posts.id,'desc':posts.desc,'created_at':posts.created_at,'user':posts.user,'image':posts.image,'credit':posts.image_credits,'mini':posts.mini_desc,'comments':comments,'comment_form': comment_form})
	else:
		posts = Forum.objects.get(id=forum_id)
		comments = Comment.objects.filter(forum = posts)
		comment_form = CommentForm()
		return render(request,'forum.html',{'title':posts.title,'id':posts.id,'desc':posts.desc,'created_at':posts.created_at,'user':posts.user,'image':posts.image,'credit':posts.image_credits,'mini':posts.mini_desc,'comments':comments,'comment_form': comment_form})

@login_required
def post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			newForum = Forum()
			newForum.user = request.user
			print(data)
			newForum.title = data['title']
			newForum.desc = data['desc']
			newForum.mini_desc = data['mini_desc']
			newForum.image = data['image']
			newForum.image_credits = data['image_credits']
			newForum.save()
			return redirect('index')
	else:
		form = PostForm()
	return render(request,'post.html',{'form': form})
	posts = Forum.objects.all()

def user_login(request):
	if request.user.is_authenticated:
		return redirect('index')
	if request.method == 'POST':
		username = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(email=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your account was inactive.")
		else:
			print("Someone tried to login and failed.")
			print("They used email: {} and password: {}".format(username,password))
			return HttpResponse("Invalid login details given")
	else:
		return render(request,'login.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
