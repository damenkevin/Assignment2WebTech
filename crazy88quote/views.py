from django.shortcuts import render
from django.utils import timezone
from .models import Quote

def post_list(request):
    quotes = Quote.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'crazy88quote/post_list.html', {'quotes': quotes})