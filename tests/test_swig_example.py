from example import get_something, set_something
from hl_example import example_handler


def test_swig_example() -> None:
    with example_handler() as h:
        assert get_something(h) == 23
        set_something(h, 42)
        assert get_something(h) == 42
