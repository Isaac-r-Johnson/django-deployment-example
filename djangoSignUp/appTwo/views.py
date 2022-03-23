from django.shortcuts import render
from appTwo.forms import SignUpForm
# Create your views here.


def index(request):
    return render(request, 'appTwo/index.html')


def users(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR, FORM INVALID")
    return render(request, 'appTwo/users.html', {'form': form})
