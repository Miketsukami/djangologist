from djangologist.morphers import BaseModelMorpher
from djangologist.selectors import BaseModelSelector
from djangologist.services import BaseService

from .models import Dummy


class DummyMorpher(BaseModelMorpher):
    model = Dummy


class DummySelector(BaseModelSelector):
    model = Dummy


class DummyService(BaseService):
    pass