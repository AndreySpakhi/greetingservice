from django.db import models


class User(models.Model):
    first_name = models.CharField('Имя пользователя', max_length=50)
    last_name = models.CharField('Фамилия пользователя', max_length=50)
    user_email = models.EmailField('Email пользователя', max_length=50, db_index=True)

    def __str__(self):
        return self.user_email


