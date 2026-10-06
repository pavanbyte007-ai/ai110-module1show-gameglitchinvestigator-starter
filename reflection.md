# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input               | Expected Behavior | Actual Behavior | Console Output / Error |
|-------              |-------------------|----------|
|Guess 69, secret 75  | Go Higher         | Go Lower         | None
|Enter key after guess| Submit Guess      | Nothing Happens  | None                  |
|change difficulty + submit guess| Show result| No result shown| None|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for Claude
- I used AI coding assistants to inspect the code, explain the bugs, and suggest minimal fixes. One correct suggestion was moving check_guess into logic_utils.py and fixing the reversed high/low messages, which I verified by running the game and testing guesses above and below the secret number. I did not accept every suggested change because some suggestions involved changing unrelated behavior, so I kept the changes limited to the required hint logic and testing.

---

## 3. Debugging and testing your fixes

- I checked whether the bug was fixed by testing guesses both below and above the secret number. I also created a pytest test that checked both the outcome and the hint message for guesses of 69 and 80 when the secret was 75. The final pytest run collected 4 tests and passed them, showing that the high/low logic was working correctly. AI helped me create the regression test and understand what the test needed to verify.
---

## 4. What did you learn about Streamlit and state?

- I learned that Streamlit reruns the Python script when the user interacts with the application, such as clicking a button. Session state is used to keep important values, such as the secret number, attempts, and score, between those reruns. Without session state, those values could be reset every time the application reruns.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is testing a bug with specific inputs before and after making a fix. Next time, I would also ask the AI to explain the existing code and propose a minimal change before allowing it to edit multiple files. This project showed me that AI-generated code can be useful, but I still need to review the changes and verify them with tests instead of assuming the AI is correct.
