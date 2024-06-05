package dmytromk.lexer.lexer.handlers;

import dmytromk.lexer.lexer.automata.Automata;
import dmytromk.lexer.lexer.token.Token;
import dmytromk.lexer.lexer.token.TokenType;

public class KeywordIdentifierHandler extends Handler {
    private final Automata keywordAutomata = new Automata(LexemesSource.KEYWORDS);
    private boolean isKeyword = false;

    @Override
    protected char charPreprocessing(char ch) {
        return Character.toLowerCase(ch);
    }

    @Override
    protected boolean includeLastChar() {
        return false;
    }

    @Override
    protected HandlingStatus appendCharQuery(char ch) {
        if (Helper.isDigit(ch) && index() == 0) {
            return HandlingStatus.REJECTED;
        }
        if (!Helper.isDigit(ch) && !Helper.isLetter(ch)) {
            if (keywordAutomata.appendString(accumulatorString()) == HandlingStatus.ACCEPTED) {
                isKeyword = true;
                return HandlingStatus.ACCEPTED;
            }
            return HandlingStatus.ACCEPTED;
        }
        return HandlingStatus.WAITING;
    }

    @Override
    protected HandlingStatus appendEOFQuery() {
        return appendCharQuery(' ');
    }

    @Override
    protected int numCharsConsumedQuery() {
        return accumulatorString().length();
    }

    @Override
    protected Token getTokenQuery() {
        if (isKeyword) {
            return new Token(TokenType.KEYWORD, accumulatorString());
        }
        return new Token(TokenType.IDENTIFIER, accumulatorString());
    }

    @Override
    protected void resetQuery() {
        keywordAutomata.reset();
        isKeyword = false;
    }
}
