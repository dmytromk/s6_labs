package dmytromk.lexer.lexer.automata;

import dmytromk.lexer.lexer.handlers.HandlingStatus;

import java.util.List;

public class Automata {
    private final State startState;
    private State currentState;
    private HandlingStatus status;
    private final StringBuilder accumulator;

    public Automata(List<String> strings) {
        this.startState = new State();
        for (String string : strings) {
            State currentState = startState;
            for (int i = 0; i < string.length(); i++) {
                char ch = string.charAt(i);
                int index = currentState.getTransValues().indexOf(ch);
                if (index == -1) {
                    State newState = new State();
                    currentState.getTransStates().add(newState);
                    currentState.getTransValues().add(ch);
                    currentState = newState;
                } else {
                    currentState = currentState.getTransStates().get(index);
                }
            }
            currentState.setAccepting(true);
        }
        this.currentState = startState;
        this.status = HandlingStatus.WAITING;
        this.accumulator = new StringBuilder();
    }

    public HandlingStatus getStatus() {
        return status;
    }

    public HandlingStatus appendChar(char ch) {
        accumulator.append(ch);
        if (status == HandlingStatus.REJECTED) {
            return HandlingStatus.REJECTED;
        }

        int index = currentState.getTransValues().indexOf(ch);
        if (index == -1) {
            status = HandlingStatus.REJECTED;
            return status;
        }
        currentState = currentState.getTransStates().get(index);
        if (currentState.isAccepting()) {
            status = HandlingStatus.ACCEPTED;
        }
        return status;
    }

    public HandlingStatus appendString(String str) {
        for (int i = 0; i < str.length(); i++) {
            appendChar(str.charAt(i));
        }
        return status;
    }

    public void reset() {
        currentState = startState;
        status = HandlingStatus.WAITING;
        accumulator.setLength(0);
    }

    @Override
    public String toString() {
        return accumulator.toString();
    }
}
