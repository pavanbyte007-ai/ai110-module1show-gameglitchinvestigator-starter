# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

## Document Your Experience

During this project, I investigated several bugs in the number guessing game and used an AI coding assistant to help analyze the code. I first reproduced the bugs manually and recorded the expected and actual behavior.

The main bug I fixed was the reversed HIGHER/LOWER hint. I also moved the `check_guess` function from `app.py` into `logic_utils.py` so the game logic could be tested separately from the Streamlit interface.

I added regression tests for the game logic and ran `pytest` to verify the changes. All 4 tests passed.

One important thing I learned was that AI suggestions still need to be reviewed and tested. I did not blindly accept every suggestion because some proposed changes were unrelated to the bugs I was investigating. The debugging process helped me understand the importance of reproducing a bug, making a small targeted change, and then testing the result.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:


1. User starts the game and enters a guess.
2. If the guess is lower than the secret number, the game displays "Go HIGHER!".
3. If the guess is higher than the secret number, the game displays "Go LOWER!".
4. The user continues entering guesses until the correct number is entered.
5. When the correct guess is entered, the game displays the win message and the score updates.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
