from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField('Отчество', max_length=25, blank=True, null=True)

    number = models.CharField('Номер телефона', max_length=18, null=True)
    date_birth = models.DateField('Дата рождения', max_length=10, blank=True, null=True)

    organization = models.CharField('Организация', max_length=100, blank=True, null=True)
    department = models.TextField('Отдел', blank=True, null=True)

