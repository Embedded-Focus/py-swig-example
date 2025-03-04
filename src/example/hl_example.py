from collections.abc import Generator
from contextlib import contextmanager

import example


class ExampleHandler:
    def __init__(self, h) -> None:
        self._h = h

    @property
    def something(self) -> int:
        return example.get_something(self._h)

    @something.setter
    def something(self, value: int) -> None:
        example.set_something(self._h, value)


@contextmanager
def example_handler() -> Generator[ExampleHandler, None, None]:
    h = None
    try:
        h = example.alloc_something()
        if h is None:
            raise RuntimeError("Could allocate something.")
        yield ExampleHandler(h)
    finally:
        if h is None:
            return

        example.free_something(h)
