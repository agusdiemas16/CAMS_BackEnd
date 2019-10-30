from django.shortcuts import render

# Create your views here.
import csv
from django.http import HttpResponse
from customerapp.models import Customer

def customer_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment ; filename=customerapp.csv'
    writer = csv.writer(response)
    customers = Customer.objects.all()

    writer.writerow(['Nama','Gaji','Jenis_Kelamin','Existing','Occupation','Alamat','Kendaraan'])
    for customer in customers:
        writer.writerow([customer.nama, customer.gaji, customer.jenis_kelamin, customer.existing, customer.occupation, customer.alamat, customer.kendaraan])

    return response