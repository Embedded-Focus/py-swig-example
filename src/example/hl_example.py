from collections.abc import Generator
from contextlib import contextmanager

import example


@contextmanager
def example_handler() -> Generator[example.Handler, None, None]:
    h = None
    try:
        h = example.alloc_something()
        if h is None:
            raise RuntimeError("Could allocate something.")
        yield h
    finally:
        if h is None:
            return
        example.free_something(h)
