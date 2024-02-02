from django.db import models

# Create your models here.
class Bakir(models.Model):
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=55)
    full_name = models.CharField(max_length=55)
    About_Me = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Информация  о  пользователе '    
        verbose_name_plural = 'Информация  о  пользователей'    
        