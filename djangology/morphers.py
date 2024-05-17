from __future__ import annotations

import abc
import typing

from .types import TModel


class BaseModelMorpher(typing.Generic[TModel], abc.ABC):
    model = type[TModel]

    @typing.final
    def __init__(self, instance: TModel) -> None:
        self.instance = instance

    @typing.final
    def add_attribute(self, name: str, value: typing.Any) -> typing.Self:
        setattr(self.instance, name, value)

        return self

    @typing.final
    def add_attributes(self, **kwargs: typing.Any) -> typing.Self:
        for attr, value in kwargs.items():
            self.add_attribute(attr, value)

        return self

    @typing.final
    def get_instance(self) -> TModel:
        return self.instance