from django.shortcuts import render

def post_list(request):
    return render(request, 'crazy88quote/post_list.html')