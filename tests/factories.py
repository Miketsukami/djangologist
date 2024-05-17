import factory

from factory import fuzzy


class RelatedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dummy_app.Related'

    value = fuzzy.FuzzyInteger(low=0, high=100)


class DummyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dummy_app.Dummy'

    value = fuzzy.FuzzyInteger(low=0, high=100)
    related = factory.SubFactory(RelatedFactory)
