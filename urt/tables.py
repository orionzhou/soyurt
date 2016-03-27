import django_tables2 as tables
from .models import Strain, Test, Phenotype, Location, Genotype, Test_location, Trial, Observation

class ObservationTable(tables.Table):
    class Meta:
        model = Observation
        attrs = {"class": "paleblue"}
