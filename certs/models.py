from django.db import models

# Create your models here.

# Need to make a Validator for Dignity of Priests: "Іерэй", "Протаіерэй", etc 
class Dignity(models.Model):
    name = models.CharField(verbose_name="Сан", max_length=100)

#    
class Clergy(models.Model):
    dignity = models.OneToOneField(Dignity, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Імя святара", max_length=100)

# Parent general class of certificates for Certificates of Baptism and Wedding    
class Certificate(models.Model):
    date = models.DateField(verbose_name="Дата")
    number = models.IntegerField(verbose_name="Нумар")
    priest = models.OneToOneField(Clergy, on_delete=models.CASCADE)

class Baptism(Certificate):
    baptized_name = models.CharField(verbose_name="Імя ахрышчанага", max_length=30)
    baptized_middle_name = models.CharField(verbose_name="Імя па бацьку ахрышчанага", max_length=30)
    baptized_surname = models.CharField(verbose_name="Прозвішча ахрышчанага", max_length=30)
    godfather = models.CharField(verbose_name="Хросны бацька", max_length=100)
    godmother = models.CharField(verbose_name="Хросная маці", max_length=100)
    saint_name = models.CharField(verbose_name="Імя святога", max_length=300)
    saint_date = models.DateField(verbose_name="Дзень Анёла")

class Wedding(Certificate):
    fiance_name = models.CharField(verbose_name="Імя жаніха", max_length=30)
    fiance_middle_name = models.CharField(verbose_name="Імя па бацьку жаніха", max_length=30)
    fiance_surname = models.CharField(verbose_name="Прозвішча жаніха", max_length=30)
    fiancee_name = models.CharField(verbose_name="Імя нявесты", max_length=30)
    fiancee_middle_name = models.CharField(verbose_name="Імя па бацьку нявесты", max_length=30)
    fiancee_surname = models.CharField(verbose_name="Прозвішча нявесты", max_length=30)
    witness1 = models.CharField(verbose_name="Сведка №1", max_length=100)
    witness2 = models.CharField(verbose_name="Сведка №2", max_length=100)
    



    