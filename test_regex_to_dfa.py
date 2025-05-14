

from regex_to_dfa import regex_to_dfa

def test_regex_to_dfa():
    dfa = regex_to_dfa("(a|b)*abb")
    assert dfa.accepts("aabb") == True
    assert dfa.accepts("ababa") == False
    assert dfa.accepts("abb") == True
    assert dfa.accepts("babb") == True
    assert dfa.accepts("ab") == False

if __name__ == "__main__":
    test_regex_to_dfa()
    print("All tests passed.")

