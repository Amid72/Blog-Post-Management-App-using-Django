from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myapp/home.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
