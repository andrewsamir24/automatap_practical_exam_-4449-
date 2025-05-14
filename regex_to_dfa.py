

from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol

class DFA:
    def __init__(self, dfa: DeterministicFiniteAutomaton):
        self.dfa = dfa

    def accepts(self, input_string: str) -> bool:
        current_state = self.dfa.start_state
        for symbol in input_string:
            current_state = self.dfa._transition_function(current_state, Symbol(symbol))
            if current_state is None:
                return False
        return current_state in self.dfa.final_states

def regex_to_dfa(regex: str) -> DFA:
    reg_expr = Regex(regex)
    nfa = reg_expr.to_epsilon_nfa()
    dfa = nfa.minimize()
    return DFA(dfa)
