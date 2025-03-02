from collections.abc import Iterator

import example
import pytest


@pytest.fixture(scope="function", name="handler")
def fixture_handler() -> Iterator[example.Handler]:
    h = example.alloc_something()
    if h is None:
        raise RuntimeError("could not allocate something")
    yield h
    example.free_something(h)


def test_swig_example(handler: example.Handler) -> None:
    assert example.get_something(handler) == 23
    example.set_something(handler, 42)
    assert example.get_something(handler) == 42
