import typing

from django.db.models import Model


TModel = typing.TypeVar('TModel', bound=Model)
