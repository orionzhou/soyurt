import django_tables2 as tables
from .models import Strain, Test, Phenotype, Location, Genotype, Test_location, Trial, Observation

class StrainTable(tables.Table):
    class Meta:
        model = Strain
        attrs = {"class": "paleblue"}
class LocationTable(tables.Table):
    class Meta:
        model = Location
        attrs = {"class": "paleblue"}
class PhenotypeTable(tables.Table):
    class Meta:
        model = Phenotype
        attrs = {"class": "paleblue"}
class TestTable(tables.Table):
    class Meta:
        model = Test
        attrs = {"class": "paleblue"}
class ObservationTable(tables.Table):
    class Meta:
        model = Observation
        attrs = {"class": "paleblue"}
