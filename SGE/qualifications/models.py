"""Qualification models"""

# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator

# Models
from users.models import User
from students.models import Student
from subjects.models import Subject


class Qualification(models.Model):
    """Qualification model"""

    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING,)

    score = ArrayField(
        base_field=models.IntegerField(
            validators=[MaxValueValidator(100)]
        ),
        size=6
    )
    final_score = models.FloatField(null=True)

    def __str__(self):
        """Return control number and subject id"""
        return f'{self.student}, {self.subject}'
