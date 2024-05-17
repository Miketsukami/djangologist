from __future__ import annotations

import abc
import typing

from django.utils import timezone


if typing.TYPE_CHECKING:
    import datetime


class BaseService(abc.ABC):
    def __init__(self, *, request_time: datetime.datetime | None = None) -> None:
        self.request_time = request_time
        if request_time is None:
            self.request_time = timezone.now()
