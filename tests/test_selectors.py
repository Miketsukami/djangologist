import pytest
import pytest_cases

from pytest_unordered import unordered

from .dummy_app.logic import DummySelector


@pytest.mark.django_db()
class TestBaseModelSelector:
    class CasesGetObject:
        def case_found(self, dummies):
            return dummies[0].pk, dummies[0]

        def case_not_found(self):
            return 0, None

    @pytest.fixture()
    def dummies(self, dummy_factory):
        return [
            dummy_factory(),
            dummy_factory(),
            dummy_factory(),
        ]

    def test_select_related(self, dummies, django_assert_num_queries):
        selector = DummySelector()
        selector.select_related('related')

        with django_assert_num_queries(1):
            result = [item.related for item in selector.get_queryset()]

        assert result == unordered([dummies[0].related, dummies[1].related, dummies[2].related])

    def test_get_queryset(self, dummies):
        queryset = DummySelector().get_queryset()

        assert list(queryset) == unordered(dummies)

    @pytest_cases.parametrize_with_cases(('pk', 'expected'), cases=CasesGetObject)
    def test_get_object(self, dummies, pk, expected):
        instance = DummySelector().get_object(pk=pk, raise_exception=False)

        assert instance == expected

    def test_pks(self, dummies):
        pks = DummySelector().pks

        assert pks == unordered([dummies[0].pk, dummies[1].pk, dummies[2].pk])
