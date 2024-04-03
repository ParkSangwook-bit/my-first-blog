from django.shortcuts import render
from django.utils import timezone
from .models import Post
# .은 현재 디렉토리 또는 애플리케이션을 의미
# 동일 디렉토리에 있는 models.py가 있기 때문에 내용을 가져올 수 있음.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# 이 함수는 요청을 넘겨받아 render 메서드를 호출한다.
# 이 render 메서드는 요청을 받아 blog/post_list.html 템플릿을 보여준다.