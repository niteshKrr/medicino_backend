
from rest_framework import serializers
from medicino.models import Cure
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
       model=Cure
       fields=['id','disease','medicine']