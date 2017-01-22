from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Representative(models.Model):
        first_name = models.CharField(max_length=200,default='')
        last_name = models.CharField(max_length=200,default='')
        
	BOR = 'BOR'
	HRONE = 'HRONE'
	NGE = 'NGE'
	CLIENT = 'CLIENT'
	SDR = 'SDR'
        ROLE_CHOICES = (
	(BOR, 'BOR AE'),
	(HRONE,'HR One AE'),
	(NGE, 'NGE AE'),
        (SDR, 'SDR'),
        (CLIENT,'Client AE'),
        )
        role = models.CharField(
                max_length=6,
                choices=ROLE_CHOICES,
                default=HRONE,
                )
        quota = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
        variable = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
        base = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
        
        def __str__(self):
                return self.first_name + ' ' + self.last_name
