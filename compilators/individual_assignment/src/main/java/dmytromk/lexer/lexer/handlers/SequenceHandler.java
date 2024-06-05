package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.automata.Automata;

import java.util.List;

public abstract class SequenceHandler extends Handler {
    private final Automata sequenceAutomata;
    private final char EOFChar;
    private int lastAcceptedIndex;

    public SequenceHandler(List<String> sequences, char EOFChar) {
        this.sequenceAutomata = new Automata(sequences);
        this.EOFChar = EOFChar;
        this.lastAcceptedIndex = -1;
    }

    @Override
    protected boolean includeLastChar() {
        return false;
    }

    @Override
    protected HandlingStatus appendCharQuery(char ch) {
        HandlingStatus status = sequenceAutomata.appendChar(ch);
        if (status == HandlingStatus.ACCEPTED) {
            lastAcceptedIndex = index();
            return HandlingStatus.WAITING;
        }
        if (status == HandlingStatus.REJECTED) {
            if (lastAcceptedIndex == -1) {
                return HandlingStatus.REJECTED;
            }



            return HandlingStatus.ACCEPTED;
        }
        return HandlingStatus.WAITING;
    }

    @Override
    protected HandlingStatus appendEOFQuery() {
        return appendCharQuery(EOFChar);
    }

    @Override
    protected int numCharsConsumedQuery() {
        return lastAcceptedIndex + 1;
    }

    @Override
    protected void resetQuery() {
        sequenceAutomata.reset();
        lastAcceptedIndex = -1;
    }
}
