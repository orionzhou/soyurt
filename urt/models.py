from __future__ import unicode_literals
from django.db import models

class Strain(models.Model):
    name = models.CharField(max_length=256)
    maternal_id = models.IntegerField(null=True, blank=True)
    paternal_id = models.IntegerField(null=True, blank=True)
    seed_source = models.CharField(max_length=45, null=True, blank=True)
    generation = models.CharField(max_length=16, null=True, blank=True)
    previous_testing = models.CharField(max_length=45, null=True, blank=True)
    unique_traits = models.CharField(max_length=256, null=True, blank=True)
    alias_pi = models.CharField(max_length=256, null=True, blank=True)
    alias_experiment = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=45)
    year = models.CharField(max_length=4)
    def __unicode__(self):
        return "%s %s" % (self.year, self.name)

class Location(models.Model):
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=16)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    geo_source = models.CharField(max_length=256, null=True, blank=True)
    geo_datum = models.CharField(max_length=32, null=True, blank=True)
    geo_resolution = models.IntegerField(null=True, blank=True)
    geo_values = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return "%s[%s]" % (self.city, self.state)

class Phenotype(models.Model):
    name = models.CharField(max_length=45)
    abbreviation = models.CharField(max_length=16)
    crop_ontology_id = models.CharField(max_length=45, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    scale = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.name

class Genotype(models.Model):
    strain = models.ForeignKey(Strain, on_delete=models.CASCADE)
    call = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    chromosome = models.CharField(max_length=16)
    position = models.IntegerField(null=True, blank=True)
    genome_release = models.CharField(max_length=45, null=True, blank=True)
    def __unicode__(self):
        return "%s:%s:%d:%s" % (self.genome_release, self.chromosome, self.position, self.call)

class Test_location(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    row_spacing = models.IntegerField(null=True, blank=True)
    rows_per_plot = models.IntegerField(null=True, blank=True)
    yield_cv = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    yield_lsd = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    note = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return "%s-%s" % (self.test, self.location)

class Trial(models.Model):
    strain = models.ForeignKey(Strain, on_delete=models.CASCADE)
    test_location = models.ForeignKey(Test_location, on_delete=models.CASCADE)
    planting_date = models.DateField()
    maturity_date = models.DateField()
    def __unicode__(self):
        return "%s-%s" % (self.test_location, self.strain)

class Observation(models.Model):
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE)
    phenotype = models.ForeignKey(Phenotype, on_delete=models.CASCADE)
    value = models.CharField(max_length=45)
    def __unicode__(self):
        return "%s-%s" % (self.trial, self.phenotype)

