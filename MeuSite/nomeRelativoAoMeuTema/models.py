from django.db import models

# Create your models here.
 
class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='NAME') # Field name made lowercase.
    mpg = models.FloatField(db_column='MPG') # Field name made lowercase.
    cyl = models.IntegerField(db_column='CYL') # Field name made lowercase.
    disp = models.FloatField(db_column='DISP') # Field name made lowercase.
    hp = models.IntegerField(db_column='HP') # Field name made lowercase.
    wt = models.FloatField(db_column='WT') # Field name made lowercase.
    sec = models.FloatField(db_column='QSEC') # Field name made lowercase.
    vs = models.IntegerField(db_column='VS') # Field name made lowercase.
    am = models.IntegerField(db_column='AM') # Field name made lowercase.
    gear = models.IntegerField(db_column='GEAR') # Field name made lowercase.
    
    def __str__(self):
        return f'Carro: {self.name}'
        