from django.db import models


class Project(models.Model):
    project = models.CharField(max_length=50, verbose_name='Проект')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    date_start = models.CharField(max_length=20, null=False, blank=False, verbose_name='Начало')
    date_end = models.CharField(max_length=20, null=False, blank=False, verbose_name='Завершение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')

    def __str__(self):
        return self.project
