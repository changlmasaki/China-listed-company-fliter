from django.db import models


# Create your models here.

class List(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    abbr = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    main_income = models.CharField(max_length=255, blank=True, null=True)
    benefits = models.CharField(max_length=255, blank=True, null=True)
    staffs = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    book = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.CharField(max_length=255, blank=True, null=True)
    job_category = models.CharField(max_length=255, blank=True, null=True)
    product_category = models.CharField(max_length=255, blank=True, null=True)
    main_duty = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'mysite_echarts_list'

