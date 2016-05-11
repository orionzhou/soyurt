from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Strain, Test, Phenotype, Location, Genotype, Test_location, Trial, Observation
from .tables import ObservationTable, StrainTable, LocationTable, PhenotypeTable, TestTable

def home(request):
    return render(request, 'home.html', {})
def strains(request):
    table = StrainTable(Strain.objects.order_by('id'))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, 'show_table.html', {"table": table})
def locations(request):
    table = LocationTable(Location.objects.order_by('id'))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, 'show_table.html', {"table": table})
def phenotypes(request):
    table = PhenotypeTable(Phenotype.objects.order_by('id'))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, 'show_table.html', {"table": table})
def tests(request):
    table = TestTable(Phenotype.objects.order_by('id'))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, 'show_table.html', {"table": table})
def observations(request):
    table = ObservationTable(Observation.objects.order_by('trial'))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, 'show_table.html', {"table": table})
