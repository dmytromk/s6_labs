package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.exceptions.LexicalException;
import dmytromk.lexer.lexer.token.Token;

public abstract class Handler {
    private Token token = null;
    private HandlingStatus status = HandlingStatus.WAITING;
    private int index = 0;
    private final StringBuilder accumulator = new StringBuilder();

    private void handleStatus(char ch) {
        if (status == HandlingStatus.ACCEPTED) {
            if (accumulator.isEmpty()) {
                status = HandlingStatus.REJECTED;
                handleStatus(ch);
                return;
            }
            if (includeLastChar()) {
                index++;
                accumulator.append(ch);
            }
            token = getTokenQuery();
        } else if (status == HandlingStatus.WAITING) {
            index++;
            accumulator.append(ch);
        }
    }

    public Token getToken() {
        return token;
    }

    public HandlingStatus getStatus() {
        return status;
    }
    
    public HandlingStatus appendChar(char ch) throws LexicalException {
        if (status != HandlingStatus.WAITING) {
            return null;
        }
        ch = charPreprocessing(ch);
        status = appendCharQuery(ch);
        handleStatus(ch);
        return status;
    }

    public HandlingStatus appendEOF() throws LexicalException {
        if (status != HandlingStatus.WAITING) {
            return null;
        }
        status = appendEOFQuery();
        return status;
    }

    public int numCharsConsumed() {
        if (status != HandlingStatus.ACCEPTED) {
            return -1;
        }
        return numCharsConsumedQuery();
    }

    public void reset() {
        resetQuery();
        token = null;
        status = HandlingStatus.WAITING;
        index = 0;
        accumulator.setLength(0);
    }

    protected int index() {
        return index;
    }

    protected String accumulatorString() {
        return accumulator.toString();
    }

    protected char charPreprocessing(char ch) {
        return ch;
    }

    protected boolean includeLastChar() {
        return true;
    }

    protected abstract HandlingStatus appendCharQuery(char ch) throws LexicalException;
    protected abstract HandlingStatus appendEOFQuery() throws LexicalException;
    protected abstract int numCharsConsumedQuery();
    protected abstract Token getTokenQuery();
    protected abstract void resetQuery();
}
