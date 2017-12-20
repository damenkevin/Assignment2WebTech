from django.shortcuts import render
from django.utils import timezone
from .models import Quote
from .forms import QuoteForm

def quote(request):
    quotes = Quote.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    number = Quote.objects.count() % 2
    form = QuoteForm()
    return render(request, 'crazy88quote/quote.html', {'quotes': quotes, 'number':number, 'form':form})

def crazy88(request):

    return render(request, 'crazy88quote/crazy88.html', {})