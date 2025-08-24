import pytest
from toolbox import text, units


def test_text_stats():
    s = text.text_stats("the cat the dog")
    assert s == {"characters": 15, "words": 4, "lines": 1, "unique_words": 3}


def test_slug_and_hash():
    assert text.slugify("Hello, World!") == "hello-world"
    assert text.hash_text("abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    with pytest.raises(ValueError):
        text.hash_text("x", "nope")


def test_unit_conversion():
    assert units.convert(1, "km", "m") == 1000
    assert round(units.convert(100, "c", "f"), 1) == 212.0
    assert round(units.convert(1, "kg", "lb"), 4) == 2.2046
    with pytest.raises(ValueError):
        units.convert(1, "kg", "m")
