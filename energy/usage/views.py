from django.shortcuts import render, redirect
from .models import Rate, Customer, CustomerReading, File
from .forms import upload_form
import types

# Create your views here.
def home(request):
    File.objects.all().delete()

    if request.method == 'POST':
        form = upload_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('The file is saved')
    else:
        form = upload_form()

    if CustomerReading.objects.all().count()>0:
        readings = CustomerReading.objects.filter(number=2)
        rates = Rate.objects.all()
        winners = []
        for r in rates:
            sorted_data = sorted(readings.filter(rate=r), key=lambda a: a.consumption(), reverse=True)
            r.readings = sorted_data
            if r.name in ['Day Rate', 'Night Rate']:
                winners.append(sorted_data[0])

        customers = Customer.objects.all().prefetch_related('customerreading')
        for c in customers:
            c.total_consumption = 0
            for r in c.customerreading.filter(number=2):
                c.total_consumption+=r.consumption()

        highest_consumption_customer = sorted(customers, key=lambda a: a.total_consumption, reverse=True)[0]

        #Rate.objects.all().prefetch_related('customerreading'),



        data = {
            'rates': rates,
            'winners':winners,
            'highest_consumption_customer': highest_consumption_customer,
            'form': form,
        }
    else:
        return render(request, 'usage/home.html', {'form':form})
    return render(request, 'usage/home.html', data)


def upload(request):
    if request.method == 'POST':
        form = upload_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return HttpResponse('The file is saved')
    else:
        form = upload_form()
        context = {
            'form': form,
        }

def clear(request):
    CustomerReading.objects.all().delete()
    Customer.objects.all().delete()
    Rate.objects.all().delete()
    File.objects.all().delete()

    return redirect('home')