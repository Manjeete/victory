from django.shortcuts import render
from .models import Menu
from home.bookinginfo import select_day, select_time, persons

# Create your views here.
def menu(request):
    breakfasts = Menu.objects.filter(menu_type='Breakfast Menu')
    lunches = Menu.objects.filter(menu_type='Lunch Menu')
    dinners = Menu.objects.filter(menu_type='Dinner Menu')

    context = {
        'breakfasts':breakfasts,
        'lunches':lunches,
        'dinners':dinners,
        'select_day':select_day,
        'select_time':select_time,
        'persons':persons
    }

    return render(request, 'menu/menu.html', context)
