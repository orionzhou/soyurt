from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Strain, Test, Phenotype, Location, Genotype, Test_location, Trial, Observation
from .tables import ObservationTable

def observations(request):
    table = ObservationTable(Observation.objects.order_by('trial'))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, 'observations.html', {"table": table})
