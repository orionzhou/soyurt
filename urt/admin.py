from django.contrib import admin

from .models import Strain, Test, Location, Phenotype, Observation, Test_location, Trial, Genotype 

admin.site.register(Strain)
admin.site.register(Test)
admin.site.register(Location)
admin.site.register(Phenotype)
admin.site.register(Observation)
admin.site.register(Test_location)
admin.site.register(Trial)
admin.site.register(Genotype)

