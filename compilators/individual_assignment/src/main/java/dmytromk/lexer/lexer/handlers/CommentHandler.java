package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.exceptions.LexicalException;
import dmytromk.lexer.lexer.automata.Automata;
import dmytromk.lexer.lexer.token.Token;
import dmytromk.lexer.lexer.token.TokenType;

import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

public class CommentHandler extends Handler {
    private boolean inComment = false;
    private final Automata startAutomata = new Automata(LexemesSource.LEFT_COMMENTS);
    private final List<Automata> endAutomatonsList = new LinkedList<>();

    @Override
    protected HandlingStatus appendCharQuery(char ch) {
        if (!inComment) {
            HandlingStatus status = startAutomata.appendChar(ch);
            if (status == HandlingStatus.REJECTED) {
                return HandlingStatus.REJECTED;
            }
            if (status == HandlingStatus.ACCEPTED) {
                inComment = true;
            }
            return HandlingStatus.WAITING;
        }

        endAutomatonsList.add(new Automata(LexemesSource.RIGHT_COMMENTS));
        ListIterator<Automata> iterator = endAutomatonsList.listIterator();
        while (iterator.hasNext()) {
            Automata automata = iterator.next();
            HandlingStatus status = automata.appendChar(ch);
            if (status == HandlingStatus.REJECTED) {
                iterator.remove();
            }
            if (status == HandlingStatus.ACCEPTED) {
                return HandlingStatus.ACCEPTED;
            }
        }
        return HandlingStatus.WAITING;
    }

    @Override
    protected HandlingStatus appendEOFQuery() throws LexicalException {
        if (inComment) {
            throw new LexicalException("Unclosed comment.");
        }
        return HandlingStatus.REJECTED;
    }

    @Override
    protected int numCharsConsumedQuery() {
        return accumulatorString().length();
    }

    @Override
    protected Token getTokenQuery() {
        return new Token(TokenType.COMMENT, accumulatorString());
    }

    @Override
    protected void resetQuery() {
        inComment = false;
        startAutomata.reset();
        endAutomatonsList.clear();
    }
}
