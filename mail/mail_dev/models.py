from django.db import models

class UserMail(models.Model):
    ID = models.AutoField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=50, verbose_name='Имя')
    LAST_NAME = models.CharField(max_length=50, verbose_name='Фамилия')
    BIRTHDAY = models.DateField(auto_now_add=False)
    TIMESENT = models.DateField(auto_now_add=False)
    MAIL = models.CharField(max_length=50, verbose_name='Почта')
    STATUS = models.CharField(max_length=20, verbose_name='Статус отправки', default='Не отправлено')
    def __str__(self):
        return 'Имя - {0}, Фамилия - {1}, почта - {2}'.format(self.FIRST_NAME, self.LAST_NAME, self.MAIL)
