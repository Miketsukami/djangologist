from __future__ import annotations

import abc
import typing
import warnings

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.models import Q

from .exceptions import SelectorException
from .types import TModel


if typing.TYPE_CHECKING:  # pragma: nocover
    from django.db.models import QuerySet


class BaseModelSelector(typing.Generic[TModel], abc.ABC):
    model: type[TModel]

    @typing.final
    def __init__(self, queryset: QuerySet[TModel] | None = None) -> None:
        if queryset is None:
            queryset = self.model.objects.all()

        self.queryset = queryset

    @typing.final
    def __enter__(self) -> typing.Self:
        return self

    @typing.final
    def __exit__(self, exc_type: typing.Any, exc_val: typing.Any, exc_tb: typing.Any) -> None:
        pass

    @typing.final
    def generic_search(
        self, *, query: str | None, lookups: typing.Iterable[str], ordering: typing.Iterable[str]
    ) -> typing.Self:
        self.queryset = self.queryset.order_by(*ordering)

        if query is None:
            return self

        q = Q()
        for lookup in lookups:
            q |= Q(**{lookup: query})

        self.queryset = self.queryset.filter(q)

        return self

    @typing.final
    def _search(
        self, *, query: str | None, lookups: typing.Iterable[str], ordering: typing.Iterable[str]
    ) -> typing.Self:
        warnings.warn('Please use `generic_search` instead of `_search`', DeprecationWarning, stacklevel=2)
        return self.generic_search(query=query, lookups=lookups, ordering=ordering)

    @typing.final
    def select_related(self, *lookups: str) -> typing.Self:
        self.queryset = self.queryset.select_related(*lookups)
        return self

    @typing.final
    def select_by_pks(self, *, pks: typing.Iterable[typing.Any]) -> typing.Self:
        self.queryset = self.queryset.filter(pk__in=pks)
        return self

    @typing.final
    def get_queryset(self) -> QuerySet[TModel]:
        return self.queryset

    @typing.final
    def get_object(self, *, raise_exception: bool = True, **params: typing.Any) -> TModel | None:
        try:
            return self.queryset.get(**params)
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            if raise_exception:
                raise SelectorException(e) from e

    @typing.final
    @property
    def pks(self) -> list[int]:
        return list(self.queryset.values_list('pk', flat=True))
