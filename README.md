# Automata Practical Exam <4449>

## Section Number
Section 2

## Section Name
Regular Expression to DFA Converter

## Task Being Solved
Write a program that converts a regular expression to a DFA and simulates the DFA on a list of strings.

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the test:
```bash
python test_regex_to_dfa.py
```

## Files Included
- `regex_to_dfa.py`: Main logic for converting regex to DFA.
- `test_regex_to_dfa.py`: Unit tests for the DFA.
- `requirements.txt`: Python dependencies.


---



## Section Name
PDA Palindrome Checker

## Task Being Solved
Simulate a PDA that checks whether an input string belongs to a context-free language of odd-length palindromes.

## How to Run
1. No additional dependencies needed.
2. Run the test:
```bash
python test_pda_palindrome.py
```

## Notes
- Strings must be palindromes and of **odd length**.




### Task being solved:
Convert a given regular expression (e.g., `(a|b)*abb`) into a **Deterministic Finite Automaton (DFA)**, then simulate the DFA to check if it accepts or rejects input strings.

### Brief instructions to run and test:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. To run the DFA test:
   ```bash
   python test_regex_to_dfa.py
   ```
3. If `All tests passed.` is printed, the DFA is working as expected.

---


### Task being solved:
Simulate a **Pushdown Automaton (PDA)** to verify if an input string is an **odd-length palindrome**. The PDA uses a stack to match characters symmetrically before and after the middle character.

### Brief instructions to run and test:
1. No additional dependencies required.
2. To run the PDA test:
   ```bash
   python test_pda_palindrome.py
   ```
3. If `All PDA tests passed.` is printed, the PDA simulation is working correctly.
# automatap_practical_exam_-4449-
