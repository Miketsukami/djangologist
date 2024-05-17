import pytest

from .dummy_app.logic import DummyMorpher


@pytest.mark.django_db()
class TestBaseModelMorpher:
    @pytest.fixture()
    def dummy(self, dummy_factory):
        return dummy_factory(value=1)

    def test_add_attributes(self, dummy):
        morpher = DummyMorpher(dummy)
        morpher.add_attributes(extra_attribute=dummy.value + 1)

        instance = morpher.get_instance()

        assert instance.extra_attribute == 2
