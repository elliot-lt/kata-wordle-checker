# Create a wordle validator
# YNMMN
# Y - This is the right letter in the right place
# M - This is the right letter but the wrong place
# N - Ths is the wrong letter

WORD_LENGTH = 5

class NotFiveLetterError(Exception):
    pass

class InvalidWordError(Exception):
    pass

def validate(guess: str, target: str) -> str:
    if len(guess) != WORD_LENGTH:
        raise NotFiveLetterError(f"whoopsie you've supplied a {len(guess)} word")
    if len(target) != WORD_LENGTH:
        raise NotFiveLetterError(f"oops, target {target} is too short: {len(target)}")
    
    exp_target = list(target)
    result = ["N"] * WORD_LENGTH
    for i, (a, b) in enumerate(zip(guess, exp_target)):
        if a == b:
            result[i] = "Y"
            exp_target[i] = None

    for i, (a, r) in enumerate(zip(guess, result)):
        if r == "Y":
            continue
        try:
            exp_i = exp_target.index(a)
        except ValueError:
            pass  # guessed letter is not in word at all
        else:
            result[i] = "M"
            exp_target[exp_i] = None

    return "".join(result)