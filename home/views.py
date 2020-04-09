from django.shortcuts import render, redirect
from menu.models import Menu
from blogs.models import Blogs
from home.bookinginfo import select_day, select_time, persons
from django.contrib import messages
from .models import CustomerInfo
from contact.models import ContactInfo
import csv

# Create your views here.


def index(request):
    menus = Menu.objects.all().filter(id__in=(1, 4, 7))
    blogs = Blogs.objects.order_by('-blog_date')[:4]

    context = {
        'menus': menus,
        'blogs': blogs,
        'select_day': select_day,
        'select_time': select_time,
        'persons': persons
    }

    return render(request, 'home/index.html', context)


def booking(request):
    if request.method == 'POST':
        day = request.POST['day']
        time = request.POST['hour']
        name = request.POST['name']
        phone = request.POST['phone']
        persons = request.POST['persons']

        customerinfo = CustomerInfo(
            day=day, time=time, name=name, phone=phone, no_of_person=persons)
        customerinfo.save()
        messages.success(request, 'Your table is confirmed')
        return redirect('/')

    return


def newsletter(request):
    if request.method == 'POST':
        email2 = request.POST['email2']
        with open('newsdata.csv', mode='a') as database:
            csv_writer = csv.writer(database)
            csv_writer.writerow([email2])
            return redirect('/')

    return
