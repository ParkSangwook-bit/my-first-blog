from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# 이 함수는 요청을 넘겨받아 render 메서드를 호출한다.
# 이 render 메서드는 요청을 받아 blog/post_list.html 템플릿을 보여준다.