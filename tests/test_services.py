import datetime

import freezegun
import pytest
import pytest_cases

from .dummy_app.logic import DummyService


class TestBaseService:
    class CasesRequestTime:
        def case_none(self, current_time):
            return None, current_time

        def case_explicit(self, another_time):
            return another_time, another_time

    @pytest.fixture()
    def current_time(self):
        return datetime.datetime.fromisoformat('2023-01-01 12:00:00+03:00')

    @pytest.fixture()
    def another_time(self):
        return datetime.datetime.fromisoformat('2023-01-02 12:00:00+03:00')

    @pytest_cases.parametrize_with_cases(('request_time', 'expected'), cases=CasesRequestTime)
    def test_request_time(self, current_time, request_time, expected):
        with freezegun.freeze_time(current_time):
            service = DummyService(request_time=request_time)

        assert service.request_time == expected
