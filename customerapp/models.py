from django.db import models

JENIS_KELAMIN = (
    ('L','Laki-Laki'),('P','Perempuan')
)

OCCUPATION = (
    ('N','Non-Fix'),('F','Fix')
)

# Create your models here.
class Customer(models.Model):
    nama = models.fields.CharField(max_length=255)
    jenis_kelamin = models.fields.CharField(max_length=1, choices=JENIS_KELAMIN, default='L')
    gaji = models.fields.FloatField()
    existing = models.fields.BooleanField()
    occupation = models.fields.CharField(max_length=1, choices=OCCUPATION, default='N') #FIX / NONFIX
    alamat = models.fields.TextField()

    def __str__(self):
        return self.nama

    def __repr__(self):
        return self.nama
