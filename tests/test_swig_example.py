from hl_example import example_handler


def test_swig_example() -> None:
    with example_handler() as h:
        assert h.something == 23
        h.something = 42
        assert h.something == 42
