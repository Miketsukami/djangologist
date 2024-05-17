from djangology.morphers import BaseModelMorpher
from djangology.selectors import BaseModelSelector
from djangology.services import BaseService

from .models import Dummy


class DummyMorpher(BaseModelMorpher):
    model = Dummy


class DummySelector(BaseModelSelector):
    model = Dummy


class DummyService(BaseService):
    pass