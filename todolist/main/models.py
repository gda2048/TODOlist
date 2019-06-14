from django.db import models


class Card(models.Model):
    """
    Stores all information about the TODOlist item
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=500)
    is_archived = models.BooleanField('Архивировано', default=False)

    def __str__(self):
        return str(self.name)