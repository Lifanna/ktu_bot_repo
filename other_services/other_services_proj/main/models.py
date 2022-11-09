from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.

class Program(models.Model):
    name = models.CharField("Наименование специальности", max_length=30, null=False, blank=False)


class Group(models.Model):
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)

    year = models.IntegerField("Год", null=False, blank=False, validators=[
            MaxValueValidator(2022),
            MinValueValidator(2019)
    ])

    order = models.IntegerField("Номер группы", null=False, blank=False)


class Student(models.Model):
    stud_identificator = models.CharField("ИИН студента", max_length=12, null=False, blank=False)

    first_name = models.CharField("Имя студента", max_length=30, null=False, blank=True, default="")

    last_name = models.CharField("Фамилия студента", max_length=30, null=False, blank=True, default="")

    grade = models.IntegerField("Курс обучения", null=False, blank=False)

    # program = models.ForeignKey(Program, on_delete=models.SET_NULL)

    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)


class DocumentSubType(models.Model):
    name = models.CharField("Наименование подтипа документа", max_length=100, null=False, blank=False)


class DocumentType(models.Model):
    name = models.CharField("Наименование типа документа", max_length=100, null=False, blank=False)

    document_sub_type = models.ForeignKey(DocumentSubType, null=True, on_delete=models.SET_NULL)


class Document(models.Model):
    document_type = models.ForeignKey(DocumentType, null=True, on_delete=models.SET_NULL)

    path = models.FileField("Ссылка на файл", upload_to='storage')

    created_at = models.DateTimeField("Дата выдачи", default=timezone.now)
