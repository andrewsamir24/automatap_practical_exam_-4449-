from pda_palindrome import PDA

def test_pda_palindrome():
    pda = PDA()
    assert pda.accepts("a") == True
    assert pda.accepts("aba") == True
    assert pda.accepts("abcba") == True
    assert pda.accepts("racecar") == True

    assert pda.accepts("aa") == False
    assert pda.accepts("abca") == False
    assert pda.accepts("ab") == False
    assert pda.accepts("") == False

if __name__ == "__main__":
    test_pda_palindrome()
    print("All PDA tests passed.")
