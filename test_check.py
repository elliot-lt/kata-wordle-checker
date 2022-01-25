import pytest
import check

def test_boring():
    check.validate("ABCDEF", "WORDS")
