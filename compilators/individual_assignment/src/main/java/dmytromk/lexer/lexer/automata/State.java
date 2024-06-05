package dmytromk.lexer.lexer.automata;

import java.util.ArrayList;

public class State {
    private final ArrayList<Character> transValues;
    private final ArrayList<State> transStates;
    private boolean isAccepting;

    public State() {
        this.transValues = new ArrayList<>();
        this.transStates = new ArrayList<>();
        this.isAccepting = false;
    }

    public void setAccepting(boolean accepting) {
        isAccepting = accepting;
    }

    public ArrayList<Character> getTransValues() {
        return transValues;
    }

    public ArrayList<State> getTransStates() {
        return transStates;
    }

    public boolean isAccepting() {
        return isAccepting;
    }
}
