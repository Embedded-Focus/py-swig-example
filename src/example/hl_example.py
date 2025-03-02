from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import dataclass

import example


@dataclass
class ExampleHandler:
    _h: example.Handler

    @property
    def something(self) -> int:
        return example.get_something(self._h)

    @something.setter
    def something(self, value: int) -> None:
        example.set_something(self._h, value)


@contextmanager
def example_handler() -> Generator[ExampleHandler, None, None]:
    h: example.Handler | None = None
    try:
        h = example.alloc_something()
        if h is None:
            raise RuntimeError("Could allocate something.")
        yield ExampleHandler(h)
    finally:
        if h is None:
            return
        example.free_something(h)
