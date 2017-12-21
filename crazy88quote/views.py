from django.shortcuts import render
from django.utils import timezone
from .models import Quote
from .forms import QuoteForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url='/login/') #redirect when user is not logged in
def quote(request):
    quotes = Quote.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    number = Quote.objects.count() % 2
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.author = request.user
            quote.published_date = timezone.now()
            quote.save()
            return redirect('quote_detail')
    else:
        form = QuoteForm()
    return render(request, 'crazy88quote/quote.html', {'quotes': quotes, 'number':number, 'form':form})

def quote_detail(request):
    quotes = Quote.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    number = Quote.objects.count() % 2
    return render(request, 'crazy88quote/quote.html', {'quotes': quotes, 'number':number})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
