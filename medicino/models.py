from django.db import models

# Create your models here.
class Cure(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    disease=models.CharField(max_length=500)
    medicine=models.CharField(max_length=200)
