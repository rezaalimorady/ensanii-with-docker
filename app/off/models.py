from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Off(models.Model):
    name = models.CharField(max_length=256, verbose_name='code name')
    code = models.CharField(max_length=20, unique=True)
    date_create = models.DateField(auto_now_add=True)
    expired_at = models.DateField(verbose_name='Expired date')
    status = models.BooleanField(default=True, verbose_name='status')
    ctrated_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created by', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Off Code'
        verbose_name_plural = 'Off Codes'


class UseCodeByUser(models.Model):
    code = models.ForeignKey(Off, on_delete=models.CASCADE, verbose_name='code')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='user')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.code.code)
