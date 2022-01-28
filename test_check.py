import pytest
import check


def test_all_wrong():
    assert check.validate("ABCDE", "WORMS") == "NNNNN"


def test_output_matches_input_length():
    assert len(check.validate("ABCDE", "WORDS")) == check.WORD_LENGTH

@pytest.mark.parametrize("guess, target", (("ADGF", "WORDS"), ("ABCDE", "WORD"), ("ADAGES", "WORDS"), ("SAND", "PIER")))
def test_wrong_length_raises_error(guess, target):
    with pytest.raises(check.NotFiveLetterError):
        check.validate(guess, target)

def test_all_right():
    assert check.validate("WORDS", "WORDS")== "YYYYY"

def test_right_letter_wrong_place():
    assert check.validate("SWORD", "WORDS") == "MMMMM"

@pytest.mark.parametrize("guess, target, expected", (
    ("SABRE", "CAPER", "NYNMM"),
    ("MUMMY", "YUMMY", "NYYYY"),
    ("CHILL", "LEMON", "NNNMN"),
))
def test_exercise_ymn_cases(guess, target, expected):
    assert check.validate(guess, target) == expected