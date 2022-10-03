from django.shortcuts import render
from .models import Article

def all_blogs(request):
  articles = Article.objects.all()
  return render(request, 'blog/all_blogs.html', {'articles':articles})
