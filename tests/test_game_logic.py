from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_direction_for_high_and_low_guesses():
    # Regression: hints were reversed (a low guess said "Go LOWER!").
    # Secret 75: guessing 69 is too low, so the player must go HIGHER.
    outcome, message = check_guess(69, 75)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message

    # Secret 75: guessing 80 is too high, so the player must go LOWER.
    outcome, message = check_guess(80, 75)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message
