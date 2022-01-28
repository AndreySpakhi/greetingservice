from django.shortcuts import render
from .models import User
from .forms import UserForm


def home(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(user_email=form['user_email'].value()):
                return render(request, 'greetings/greeting.html',
                              {'user': form['first_name'].value(), 'greetings': 'Вже бачилися, '})
            else:
                form.save()
                return render(request, 'greetings/greeting.html',
                              {'user': form['user_email'].value(), 'greetings': 'Привіт, '})
        else:
            error = 'Форма заповнена некоректно'
    form = UserForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'greetings/home.html', context)


def greeted(request):
    users_list = User.objects.all()
    return render(request, 'greetings/greeted.html', {'users_list': users_list})

