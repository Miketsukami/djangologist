from pytest_factoryboy import register

from .factories import DummyFactory, RelatedFactory


register(DummyFactory)
register(RelatedFactory)
