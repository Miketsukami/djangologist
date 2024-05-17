from django.db import models


class Related(models.Model):
    value = models.IntegerField()

    class Meta:
        verbose_name = 'Related'
        verbose_name_plural = 'Related'

    def __str__(self) -> str:  # pragma: nocover
        return self.pk


class Dummy(models.Model):
    value = models.IntegerField()
    related = models.ForeignKey(Related, related_name='dummies', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Dummy'
        verbose_name_plural = 'Dummy'

    def __str__(self) -> str:  # pragma: nocover
        return self.pk
