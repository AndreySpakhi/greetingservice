from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
            error = 'Форма заповнена некоректно, перевірте правильність написання email адреси'
    form = UserForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'greetings/home.html', context)


def greeted(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 3)
    page = request.GET.get('page')
    try:
        visitors = paginator.page(page)
    except PageNotAnInteger:
        visitors = paginator.page(1)
    except EmptyPage:
        visitors = paginator.page(paginator.num_pages)
    return render(request, 'greetings/greeted.html', {'page': page, 'visitors': visitors})

